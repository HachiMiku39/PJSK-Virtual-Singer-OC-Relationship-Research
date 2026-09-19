#!/usr/bin/env python3
"""Recompute the PJSK sampled ledger using only Python's standard library.

Usage: python3 recompute.py PJSK_event_ledger.json --output PJSK_scores.json
The scores describe the supplied observations, not the unobserved full corpus.
"""
import argparse
import copy
import json
from collections import defaultdict
from pathlib import Path

BASE = {"S": 16, "A": 8, "B": 3, "C": 1, "0": 0}
VS = ["Miku", "Rin", "Len", "Luka", "MEIKO", "KAITO"]


def calculate(events, roster, exponent=2.2, merge_themes=False):
    groups = defaultdict(list)
    calculated = []
    seen = set()
    for source in events:
        e = copy.deepcopy(source)
        assert e["id"] not in seen
        seen.add(e["id"])
        assert e["oc"] in roster and e["vs"] in VS
        assert e["level"] in BASE
        assert e["agency"] in [0.85, 1, 1.1, 1.25]
        assert e["impact"] in [0.9, 1, 1.2, 1.35]
        assert e["uniqueness"] in [0.8, 1, 1.2, 1.4]
        e["base"] = BASE[e["level"]]
        e["pre_repeat_raw"] = round(e["base"] * e["agency"] * e["impact"] * e["uniqueness"], 8)
        e["repeat_rank"] = None
        e["repeat"] = 0.0
        e["event_raw"] = 0.0
        calculated.append(e)
        if e["base"]:
            theme = "ALL_THEMES" if merge_themes else e["affinity"]
            groups[(e["oc"], e["vs"], theme)].append(e)
    for group in groups.values():
        # Importance: tier first, then the pre-decay amount; ID breaks exact ties.
        group.sort(key=lambda e: (-e["base"], -e["pre_repeat_raw"], e["id"]))
        for rank, e in enumerate(group):
            e["repeat_rank"] = rank + 1
            e["repeat"] = [1.0, 0.6, 0.35][rank] if rank < 3 else 0.2
            e["event_raw"] = round(e["pre_repeat_raw"] * e["repeat"], 8)
    results = []
    for oc in roster:
        raw = {v: 0.0 for v in VS}
        affinities = {v: set() for v in VS}
        ids = {v: [] for v in VS}
        for e in calculated:
            if e["oc"] == oc:
                raw[e["vs"]] += e["event_raw"]
                ids[e["vs"]].append(e["id"])
                if e["event_raw"]:
                    affinities[e["vs"]].add(e["affinity"])
        raw = {v: round(x, 8) for v, x in raw.items()}
        maximum = max(raw.values())
        final = {v: 100 * (raw[v] / maximum) ** exponent if maximum else 0 for v in VS}
        leaders = [v for v in VS if maximum and abs(raw[v] - maximum) < 1e-8]
        # Remove exactly one maximum, retaining other maxima in the five competitors.
        d = 100 - (sum(final.values()) - 100) / 5 if maximum else None
        ordered = sorted(final.values(), reverse=True)
        if not maximum:
            shape = "无可算事件"
        elif ordered[2] >= 70:
            shape = "多P样形：至少三项≥70"
        elif ordered[1] >= 90:
            shape = "高竞争双峰：原规范未明确≥90的边界"
        elif ordered[1] >= 70:
            shape = "1S+1P样形：第二项70—90"
        elif ordered[1] < 55:
            shape = "单S样形：第二项<55"
        else:
            shape = "过渡形：原规范未定义55—70"
        results.append({
            "oc": oc, "observed_raw": raw,
            "observed_final": {v: round(x, 6) for v, x in final.items()},
            "observed_D": round(d, 6) if d is not None else None,
            "sample_leaders": leaders, "sample_shape": shape,
            "global_final": None, "global_D": None, "global_core_type": "未定",
            "global_ranking_confidence": "B：覆盖不足；不是数值概率",
            "cpu0": "Miku：结构角色另判" if oc == "朝比奈真冬" else "未专项判定",
            "scored_pairs": sum(x > 0 for x in raw.values()),
            "affinities": {v: sorted(a) for v, a in affinities.items()},
            "event_ids": ids,
        })
    return {"events": calculated, "characters": results}


def recompute(data):
    roster = data["roster"]
    events = data["events"]
    base = calculate(events, roster, data["parameters"]["exponent"])
    scenarios = {}
    downgraded = copy.deepcopy(events)
    for e in downgraded:
        if e["level"] == "S":
            e["level"] = "A"
    scenarios["all_S_to_A"] = calculate(downgraded, roster)
    scenarios["all_themes_merged_per_pair"] = calculate(events, roster, merge_themes=True)
    for oc in roster:
        original = next(x for x in base["characters"] if x["oc"] == oc)
        changes = []
        single_downgrade = []
        for e in events:
            if e["oc"] != oc or e["level"] == "0":
                continue
            sub = [x for x in events if x["id"] != e["id"]]
            out = calculate(sub, roster)
            alt = next(x for x in out["characters"] if x["oc"] == oc)
            if alt["sample_leaders"] != original["sample_leaders"]:
                changes.append({"removed_event": e["id"], "leaders": alt["sample_leaders"]})
            if e["level"] == "S":
                sub = copy.deepcopy(events)
                next(x for x in sub if x["id"] == e["id"])["level"] = "A"
                alt = next(x for x in calculate(sub, roster)["characters"] if x["oc"] == oc)
                if alt["sample_leaders"] != original["sample_leaders"]:
                    single_downgrade.append({"downgraded_event": e["id"], "leaders": alt["sample_leaders"]})
        original["sensitivity"] = {
            "leave_one_ledger_entry_out_changes": changes,
            "one_S_to_A_changes": single_downgrade,
            **{name: next(x for x in out["characters"] if x["oc"] == oc)["sample_leaders"] for name, out in scenarios.items()},
        }
    assert len(base["characters"]) == 20
    assert sum(len(x["observed_raw"]) for x in base["characters"]) == 120
    for x in base["characters"]:
        assert max(x["observed_final"].values()) == 100
        assert 0 <= x["observed_D"] <= 100
    return {
        "version": data["version"], "scope": data["scope"],
        "warning": "0 means no scored observation in this selective sample; it is not an estimate of zero global narrative importance.",
        "parameters": data["parameters"], "vs_order": VS,
        **base,
    }


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("ledger", type=Path)
    p.add_argument("--output", type=Path)
    args = p.parse_args()
    result = recompute(json.loads(args.ledger.read_text(encoding="utf-8")))
    payload = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.write_text(payload, encoding="utf-8")
    else:
        print(payload, end="")
