#!/usr/bin/env python3
"""Recount official setlist singer credits; no network or third-party packages."""
import json
import math
from pathlib import Path

SINGERS = ('初音ミク', '鏡音リン', '鏡音レン', '巡音ルカ', 'MEIKO', 'KAITO')
MIKU = SINGERS[0]


def recount(songs):
    if not songs:
        raise ValueError('Empty setlist')
    for song in songs:
        voices = song['singers']
        if not voices or len(voices) != len(set(voices)) or set(voices) - set(SINGERS):
            raise ValueError(f'Invalid singer credits: {song}')
        credit = song['credit'].replace('⾳', '音')
        if set(voices) != {name for name in SINGERS if name in credit}:
            raise ValueError(f'Credit text and parsed names differ: {song}')
    total = len(songs)
    solo = sum(song['singers'] == [MIKU] for song in songs)
    joint = sum(MIKU in song['singers'] and len(song['singers']) > 1 for song in songs)
    return {
        'total': total, 'miku_solo': solo, 'miku_joint': joint,
        'no_miku': total - solo - joint,
        'solo_percent': 100 * solo / total,
        'participation_percent': 100 * (solo + joint) / total,
        'singer_appearances': {name: sum(name in song['singers'] for song in songs) for name in SINGERS},
    }


def check(stored, actual, context):
    if stored.keys() != actual.keys():
        raise ValueError(f'{context}: summary fields differ')
    for key, value in actual.items():
        valid = math.isclose(stored[key], value, abs_tol=1e-9) if isinstance(value, float) else stored[key] == value
        if not valid:
            raise ValueError(f'{context}: {key}: {stored[key]} != {value}')


def main():
    data = json.loads(Path(__file__).with_name('mirai-setlists.json').read_text(encoding='utf-8'))
    sets = data['setlists']
    print('|来源分组|场地与日期|总曲数|Miku独唱|Miku合唱|不含Miku|独唱%|参与%|')
    print('|---|---|---:|---:|---:|---:|---:|---:|')
    groups = rows = 0
    annual = {}
    for year, configurations in sets.items():
        if year not in data['sources'] or not configurations:
            raise ValueError(f'Missing source/configuration: {year}')
        for group in configurations:
            actual = recount(group['songs'])
            check(group['summary'], actual, f'{year} {group["date"]}')
            groups += 1
            rows += actual['total']
            print(f'|{year}|{group["city"]} {group["date"]}|{actual["total"]}|{actual["miku_solo"]}|{actual["miku_joint"]}|{actual["no_miku"]}|{actual["solo_percent"]:.1f}|{actual["participation_percent"]:.1f}|')
            label = '十周年札幌（2023年2月）' if group['city'] == 'SAPPORO' else year[:4]
            annual.setdefault(label, []).append(actual)
    print('\n歌手参与曲数范围；合唱逐人计数，不能横向加总为演出总曲数。')
    print('|年份|' + '|'.join(SINGERS) + '|')
    print('|---|' + '---:|' * len(SINGERS))
    for year, summaries in annual.items():
        values = []
        for name in SINGERS:
            counts = [s['singer_appearances'][name] for s in summaries]
            low, high = min(counts), max(counts)
            values.append(str(low) if low == high else f'{low}–{high}')
        print('|' + year + '|' + '|'.join(values) + '|')
    print(f'\n核对通过：{len(sets)}个来源，{groups}份配置，{rows}条曲目记录。')


if __name__ == '__main__':
    main()
