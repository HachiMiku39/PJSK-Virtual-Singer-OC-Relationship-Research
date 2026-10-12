#!/usr/bin/env python3
"""Collect released JP story metadata and provenance; never infer relationship scores.

Full transcripts go only to the explicitly supplied scratch cache, not the manifest.
Uses Python's standard library. See README.md for scope and review requirements.
"""
import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, time, timedelta, timezone
import hashlib
import json
from pathlib import Path
import re
from urllib.error import HTTPError
from urllib.parse import quote
from urllib.request import Request, urlopen

STORY_REPO = "ci-ke/ProjectSekai-story"
MASTER_REPO = "Sekai-World/sekai-master-db-diff"
JST = timezone(timedelta(hours=9))


def fetch(url):
    request = Request(url, headers={"User-Agent": "PJSK-relationship-research/1.0"})
    with urlopen(request, timeout=45) as response:
        return response.read()


def get_json(url):
    return json.loads(fetch(url))


def digest(data):
    return hashlib.sha256(data).hexdigest()


def resolve(repo, ref):
    commit = get_json(f"https://api.github.com/repos/{repo}/commits/{quote(ref, safe='')}")
    return {"repository": repo, "commit": commit["sha"],
            "committed_at": commit["commit"]["committer"]["date"]}


def timestamp(ms):
    return datetime.fromtimestamp(ms / 1000, JST).isoformat()


def normalize(body):
    return re.sub(r"\s+", "", body)


def dialogue_bodies(text):
    # Speaker labels may include a SEKAI or flashback identity in parentheses.
    return [normalize(line.split(": ", 1)[1]) for line in text.splitlines()
            if ": " in line and not line.startswith(("(", "Skill name:", "Gacha phrase:"))]


def collect(args):
    now = datetime.now(timezone.utc)
    since = datetime.combine(datetime.fromisoformat(args.since).date(), time.min, JST)
    through = datetime.combine(datetime.fromisoformat(args.through).date(), time.max, JST)
    cutoff = min(now, through)
    if since > cutoff:
        raise ValueError("The interval starts after the publication cutoff")
    cache = args.cache_dir.resolve()
    # Prevent accidentally committing a copy of the complete story corpus.
    repo_root = Path(__file__).resolve().parents[2]
    if cache == repo_root or repo_root in cache.parents:
        raise ValueError("Use a scratch cache outside the research repository")
    cache.mkdir(parents=True, exist_ok=True)
    master = resolve(MASTER_REPO, args.master_ref)
    story = resolve(STORY_REPO, args.story_ref)
    tables, metadata = {}, []
    for name in ("events", "eventStories", "cards"):
        url = f"https://raw.githubusercontent.com/{MASTER_REPO}/{master['commit']}/{name}.json"
        data = fetch(url)
        (cache / f"{name}.json").write_bytes(data)
        tables[name] = json.loads(data)
        metadata.append({"name": name, "url": url, "sha256": digest(data)})
    events = [e for e in tables["events"] if since.timestamp()*1000 <= e["startAt"] <= cutoff.timestamp()*1000]
    event_ids = {e["id"] for e in events}
    stories = {s["eventId"]: s for s in tables["eventStories"]}
    cards = {c["id"]: c for c in tables["cards"]}
    tree = get_json(f"https://api.github.com/repos/{STORY_REPO}/git/trees/{story['commit']}?recursive=1")
    if tree.get("truncated"):
        raise ValueError("GitHub tree is truncated; cannot claim complete discovery")
    candidates = []
    for item in tree["tree"]:
        path = item["path"]
        if item["type"] != "blob" or not path.startswith("story_jp/") or not path.endswith(".txt"):
            continue
        parts = path.split("/")
        filename = parts[-1]
        if parts[1] == "event":
            match = re.match(r"(\d+)-(\d+) ", filename)
            if match and int(match[1]) in event_ids:
                ev, ep = int(match[1]), int(match[2])
                episode = next(x for x in stories[ev]["eventStoryEpisodes"] if x["episodeNo"] == ep)
                candidates.append({"id": f"e{ev:03}_{ep:02}", "kind": "event", "event_id": ev,
                                   "episode": ep, "title": episode["title"], "path": path,
                                   "page": f"https://pjsk.moe/ja-jp/story/event/{ev}/{ep}/",
                                   "raw_asset_url": "https://storage.exmeaning.com/sekai-jp-assets/event_story/"
                                   f"{stories[ev]['assetbundleName']}/scenario/{episode['scenarioId']}.json"})
        elif parts[1] == "card":
            match = re.search(r"event_(\d+)", filename)
            card_id = int(filename.split("_", 1)[0])
            if card_id in cards and since.timestamp()*1000 <= cards[card_id]["releaseAt"] <= cutoff.timestamp()*1000:
                card = cards[card_id]
                candidates.append({"id": f"c{card_id}", "kind": "card", "event_id": int(match[1]) if match else None,
                                   "card_id": card_id, "title": card["prefix"], "path": path,
                                   "release_at_jst": timestamp(card["releaseAt"]),
                                   "page": f"https://pjsk.moe/ja-jp/story/card/{card_id}/"})

    def download(row):
        row = dict(row)
        url = f"https://raw.githubusercontent.com/{STORY_REPO}/{story['commit']}/{quote(row['path'], safe='/')}"
        data = fetch(url)
        (cache / f"{row['id']}.txt").write_bytes(data)
        body = data.decode("utf-8")
        row.update({"text_url": url,
                    "citation_url": f"https://github.com/{STORY_REPO}/blob/{story['commit']}/{quote(row['path'], safe='/')}",
                    "sha256": digest(data), "line_count": len(body.splitlines()),
                    "acquisition_status": "downloaded", "review_status": "unreviewed"})
        if row["kind"] == "card":
            row["side_story_parts"] = body.count("<サイドストーリー（")
        elif args.probe_mirror:
            try:
                raw = fetch(row["raw_asset_url"])
                asset = json.loads(raw)
                (cache / f"{row['id']}.json").write_bytes(raw)
                actual = [normalize(t["Body"]) for t in asset["TalkData"]]
                row["mirror"] = {"status": "available", "sha256": digest(raw),
                                 "talkdata_count": len(actual),
                                 "ordered_bodies_equal_ignoring_whitespace": dialogue_bodies(body) == actual}
            except HTTPError as error:
                row["mirror"] = {"status": "unavailable", "http_status": error.code}
            except (OSError, ValueError, KeyError) as error:
                row["mirror"] = {"status": "error", "detail": str(error)}
        return row

    with ThreadPoolExecutor(max_workers=4) as pool:
        sources = sorted(pool.map(download, candidates), key=lambda x: x["id"])
    found = {(s["event_id"], s["episode"]) for s in sources if s["kind"] == "event"}
    missing = [{"event_id": e["id"], "episode": ep["episodeNo"]}
               for e in events for ep in stories[e["id"]]["eventStoryEpisodes"]
               if (e["id"], ep["episodeNo"]) not in found]
    # A released card absent from the text snapshot remains an explicit acquisition gap.
    included_cards = {s["card_id"] for s in sources if s["kind"] == "card"}
    gaps = [{"id": c["id"], "title": c["prefix"], "release_at_jst": timestamp(c["releaseAt"])}
            for c in cards.values() if since.timestamp()*1000 <= c["releaseAt"] <= cutoff.timestamp()*1000
            and c["id"] not in included_cards]
    manifest = {"schema_version": 1, "collected_at_utc": now.isoformat(),
                "since_jst": since.isoformat(), "publication_cutoff": cutoff.isoformat(),
                "scope": "Released event stories and card stories in interval, as available in the fixed JP text snapshot; excludes special/area/MySEKAI corpus review",
                "master_snapshot": master, "story_snapshot": story, "master_files": metadata,
                "events": [{"id": e["id"], "title": e["name"], "start_at_jst": timestamp(e["startAt"]),
                            "end_at_jst": timestamp(e["aggregateAt"]),
                            "expected_episodes": len(stories[e["id"]]["eventStoryEpisodes"]),
                            "page": f"https://pjsk.moe/ja-jp/story/event/{e['id']}/"} for e in events],
                "sources": sources, "missing_event_episodes": missing, "other_released_cards_not_acquired": gaps}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Collected {len(events)} events, {len(sources)} files; {len(missing)} missing episodes, {len(gaps)} other card gaps")
    return manifest


def verify(args):
    manifest = json.loads(args.output.read_text(encoding="utf-8"))
    sources = {s["id"]: s for s in manifest["sources"]}
    for sid, source in sources.items():
        data = (args.cache_dir / f"{sid}.txt").read_bytes()
        assert digest(data) == source["sha256"], f"Changed transcript: {sid}"
        assert len(data.decode("utf-8").splitlines()) == source["line_count"]
        if source.get("mirror", {}).get("status") == "available":
            raw = (args.cache_dir / f"{sid}.json").read_bytes()
            assert digest(raw) == source["mirror"]["sha256"]
            match = dialogue_bodies(data.decode("utf-8")) == [normalize(t["Body"]) for t in json.loads(raw)["TalkData"]]
            assert match == source["mirror"]["ordered_bodies_equal_ignoring_whitespace"]
    if args.evidence:
        ledger = json.loads(args.evidence.read_text(encoding="utf-8"))
        for record in ledger["records"]:
            for ref in record["references"]:
                source = sources[ref["source_id"]]
                assert 1 <= ref["start_line"] <= ref["end_line"] <= source["line_count"], record["id"]
        assert set(ledger["reviewed_source_ids"]) <= set(sources)
    print(f"Verified {len(sources)} transcript hashes, line counts, mirror comparisons and evidence ranges")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--since", default="2026-09-21", help="Inclusive release date, JST")
    parser.add_argument("--through", default=datetime.now(JST).date().isoformat(), help="Inclusive release date, JST; capped at current time")
    parser.add_argument("--master-ref", default="main")
    parser.add_argument("--story-ref", default="main")
    parser.add_argument("--probe-mirror", action="store_true")
    parser.add_argument("--cache-dir", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--verify", action="store_true", help="Offline integrity verification")
    parser.add_argument("--evidence", type=Path)
    args = parser.parse_args()
    if args.verify:
        verify(args)
    else:
        collect(args)


if __name__ == "__main__":
    main()
