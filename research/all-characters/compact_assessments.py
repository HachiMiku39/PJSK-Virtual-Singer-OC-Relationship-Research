#!/usr/bin/env python3
"""Normalize repeated provenance without removing evidence or changing codes."""
import argparse
import hashlib
import json
from pathlib import Path


def resolve_ref(data, ref):
    if 'source_id' not in ref:
        return ref
    source = data['source_catalog'][ref['source_id']]
    return {**source, **ref, 'url':source['url']+'#L'+str(ref['start_line'])}


def compact(data):
    if 'source_catalog' in data:
        return data
    catalog = {}
    def replace(ref):
        sid = hashlib.sha256((ref['path']+'\0'+ref['sha256']).encode()).hexdigest()[:24]
        source = {k:ref[k] for k in ('path','sha256','url')}
        source['url'] = source['url'].split('#')[0]
        if sid in catalog:
            assert catalog[sid]==source
        catalog[sid] = source
        return {'source_id':sid,**{k:v for k,v in ref.items() if k not in source}}
    for row in data['records']:
        for item in row['evidence']['historical_facts']+row['evidence']['emotion_candidates']:
            item['source'] = replace(item['source'])
        row['evidence']['manually_read_focus'] = [replace(x) for x in row['evidence']['manually_read_focus']]
    data['source_catalog'] = catalog
    data['schema_version'] = 'all-characters-provisional-normalized-1'
    return data


if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--input',type=Path,default=Path(__file__).with_name('assessments.json'))
    ap.add_argument('--output',type=Path)
    args=ap.parse_args();raw=args.input.read_bytes()
    data=compact(json.loads(raw));out=args.output or args.input
    encoded=(json.dumps(data,ensure_ascii=False,indent=2)+'\n').encode('utf-8')
    out.write_bytes(encoded)
    print(json.dumps({'before_bytes':len(raw),'after_bytes':len(encoded),'unique_source_files':len(data['source_catalog'])}))
