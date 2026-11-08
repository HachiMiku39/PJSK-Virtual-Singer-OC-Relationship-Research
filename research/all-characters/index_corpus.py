#!/usr/bin/env python3
"""Build cached, bounded research packets. Retrieval signals never assign relationship scores."""
import argparse
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import quote

VERSION = 1
OCS = ['一歌','咲希','穂波','志歩','みのり','遥','愛莉','雫','こはね','杏','彰人','冬弥','司','えむ','寧々','類','奏','まふゆ','絵名','瑞希']
ALIASES = {'Miku':['ミク','初音ミク'], 'Rin':['リン','鏡音リン'],
           'Len':['レン','鏡音レン'], 'Luka':['ルカ','巡音ルカ'],
           'MEIKO':['MEIKO','メイコ'], 'KAITO':['KAITO','カイト']}
SIGNALS = {
    'growth': re.compile('おかげ|気づ|気付|教え|言って|やってみ|試して|わかった|分かった|だから'),
    'expression': re.compile('ありがとう|嬉し|うれし|好き|会いた|大切'),
    'trust': re.compile('相談|頼|聞いて|話した|安心|不安|本音'),
    'investment': re.compile('プレゼント|贈|お返し|渡した|誘|一緒に|手伝'),
    'positioning': re.compile('大切|特別|先輩|友達|仲間|信頼|頼り')}


def identity(speaker):
    # A character acting as a girl, animal, etc. is retained as unknown.
    # Only the normal name and its literal voice label count as that OC.
    for oc in OCS:
        if speaker in (oc, oc+'の声'):
            return 'oc', oc
    for key, aliases in ALIASES.items():
        for alias in aliases:
            if speaker == alias or speaker.startswith(alias+'(') or speaker == alias+'の声':
                return 'vs', key
    return None, None


def named_target(body, vs):
    # Avoid lexical false positives such as リンゴ and トランポリン.
    return any(re.search(r'(?<![ァ-ヶA-Za-z])'+re.escape(a)+r'(?![ァ-ヶA-Za-z])', body)
               for a in ALIASES[vs])


def parse(raw, kind):
    lines = raw.decode('utf-8').splitlines()
    if kind == 'card':
        starts = [i for i,s in enumerate(lines) if s.startswith('<サイドストーリー')]
    elif kind == 'area':
        starts = [i for i,s in enumerate(lines) if re.match(r'^\d+ \d+:', s)]
    else:
        starts = [0]
    segments = []
    for j,start in enumerate(starts or [0]):
        end = starts[j+1] if j+1 < len(starts) else len(lines)
        dialogs = []
        for i in range(start,end):
            if ': ' not in lines[i] or lines[i].startswith(('(', 'Skill name:', 'Gacha phrase:')):
                continue
            speaker,body = lines[i].split(': ',1)
            kind_id,name = identity(speaker)
            dialogs.append({'line':i+1,'speaker':speaker,'body':body,'type':kind_id,'name':name})
        os = sorted({d['name'] for d in dialogs if d['type']=='oc'})
        vs = sorted({d['name'] for d in dialogs if d['type']=='vs'})
        if os and vs:
            segments.append({'start':start+1,'end':end,'ocs':os,'vs':vs,'dialogs':dialogs})
    return {'line_count':len(lines),'characters':len(raw.decode('utf-8')),'segments':segments}


def build(args):
    reviewed = set()
    if getattr(args,'reviewed_evidence',None):
        reviewed_ids = json.loads(args.reviewed_evidence.read_text(encoding='utf-8'))
        if not isinstance(reviewed_ids,list) or not all(isinstance(x,str) for x in reviewed_ids):
            raise ValueError('reviewed-evidence must be a JSON array of reviewed evidence IDs')
        reviewed = set(reviewed_ids)
    root = args.corpus_dir
    if (root/'story_jp').is_dir():
        root = root/'story_jp'
    if not root.is_dir():
        raise ValueError('corpus-dir must contain story_jp or its contents')
    args.cache_dir.mkdir(parents=True, exist_ok=True)
    manifest = args.cache_dir/'manifest.json'
    try:
        previous_paths = set(json.loads(manifest.read_text(encoding='utf-8'))['paths'])
    except (FileNotFoundError, json.JSONDecodeError, KeyError):
        previous_paths = set()
    current_paths = set()
    cached_count = parsed_count = total_characters = 0
    changed = []
    sources = {}
    candidate_windows = {}
    pairs = {oc+'/'+v:[] for oc in OCS for v in ALIASES}
    for p in sorted(root.rglob('*.txt')):
        relative = p.relative_to(root)
        kind = relative.parts[0]
        if kind not in ('main','event','card','area') or 'aprilfool' in str(relative).lower():
            continue
        path = 'story_jp/'+relative.as_posix()
        current_paths.add(path)
        raw = p.read_bytes()
        digest = hashlib.sha256(raw).hexdigest()
        cache_path = args.cache_dir/(hashlib.sha256(path.encode()).hexdigest()+'.json')
        try:
            old = json.loads(cache_path.read_text(encoding='utf-8'))
        except (FileNotFoundError, json.JSONDecodeError):
            old = {}
        unchanged = old.get('version')==VERSION and old.get('sha256')==digest
        if unchanged:
            parsed = old['parsed']
            cached_count += 1
        else:
            parsed = parse(raw,kind)
            cache_path.write_text(json.dumps({'version':VERSION,'sha256':digest,'parsed':parsed},ensure_ascii=False),encoding='utf-8')
            parsed_count += 1
            changed.append(path)
        total_characters += parsed['characters']
        if args.changed_only and unchanged:
            continue
        source_id = hashlib.sha256((path+'\0'+digest).encode()).hexdigest()[:24]
        for s in parsed['segments']:
            ds = s['dialogs']
            for oc in s['ocs']:
                for vs in s['vs']:
                    pair = oc+'/'+vs
                    for i,d in enumerate(ds):
                        if d['type']!='oc' or d['name']!=oc:
                            continue
                        dimensions = [k for k,rx in SIGNALS.items() if rx.search(d['body'])]
                        if not dimensions:
                            continue
                        explicit = named_target(d['body'],vs)
                        adjacent = i>0 and ds[i-1]['type']=='vs' and ds[i-1]['name']==vs
                        if not explicit and not adjacent:
                            continue
                        mode = 'explicit_name' if explicit else 'adjacent_reply_unconfirmed'
                        # The candidate is reviewable, including speakers before and after.
                        window = ds[max(0,i-2):min(len(ds),i+3)]
                        start,end = window[0]['line'],window[-1]['line']
                        evidence_id = hashlib.sha256(f'{source_id}:{start}:{end}'.encode()).hexdigest()[:24]
                        if evidence_id in reviewed:
                            continue
                        text = '\n'.join(f"L{x['line']} {x['speaker']}: {x['body']}" for x in window)
                        candidate_windows[evidence_id] = {'source_id':source_id,'start_line':start,'end_line':end,'text':text}
                        pairs[pair].append({'evidence_id':evidence_id,'dimensions':dimensions,'target_mode':mode,
                                            'retrieval_priority':(4 if explicit else 1)+len(dimensions)})
                        sources[source_id] = {'path':path,'sha256':digest,'line_count':parsed['line_count'],
                            'url':f'https://github.com/ci-ke/ProjectSekai-story/blob/{args.source_commit}/{quote(path)}'}
    removed = sorted(previous_paths-current_paths)
    manifest.write_text(json.dumps({'paths':sorted(current_paths)},ensure_ascii=False),encoding='utf-8')
    if args.pair:
        if args.pair not in pairs:
            raise ValueError('unknown pair: '+args.pair)
        pairs = {args.pair:pairs[args.pair]}
    pools = {}
    for pair,items in pairs.items():
        # Diverse retrieval: prefer different source files before repeated windows.
        items.sort(key=lambda x:(-x['retrieval_priority'],x['evidence_id']))
        seen = set()
        distinct, repeats = [], []
        for item in items:
            source = candidate_windows[item['evidence_id']]['source_id']
            if source in seen:
                repeats.append(item)
            else:
                seen.add(source)
                distinct.append(item)
        pools[pair] = distinct+repeats
    selected = {p:[] for p in pairs}
    windows = {}
    used = 0
    # Round-robin reserves coverage instead of exhausting the budget on one OC.
    # The budget includes repeated ID references and window text, not JSON metadata.
    for rank in range(args.top_k):
        for pair,pool in pools.items():
            if rank>=len(pool):
                continue
            item = pool[rank]
            eid = item['evidence_id']
            extra = len(json.dumps(item,ensure_ascii=False))+len(pair)
            if eid not in windows:
                extra += len(candidate_windows[eid]['text'])
            if used+extra>args.max_characters:
                continue
            used += extra
            selected[pair].append(item)
            windows[eid] = candidate_windows[eid]
    selected_sources = {w['source_id'] for w in windows.values()}
    result = {'schema_version':1,'source_commit':args.source_commit,
        'warning':'检索优先级仅用于选证据；相邻回复未确认对象；没有生成任何成长或情感分数。',
        'stats':{'cached_files':cached_count,'parsed_files':parsed_count,'changed_files':len(changed),
                 'removed_files':len(removed),
                 'eligible_corpus_characters':total_characters,'evidence_payload_characters':used,
                 'unique_windows':len(windows),'pairs_with_candidates':sum(bool(x) for x in selected.values()),
                 'pairs_with_retrieval_hits':sum(bool(x) for x in pools.values()),
                 'reviewed_ids_supplied':len(reviewed),
                 'selected_pair_references':sum(map(len,selected.values()))},
        'changed_paths':changed,'removed_paths':removed,'sources':{k:sources[k] for k in sorted(selected_sources)},
        'evidence':windows,'pairs':selected}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result['stats'],ensure_ascii=False))


if __name__=='__main__':
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--corpus-dir',type=Path,required=True)
    ap.add_argument('--cache-dir',type=Path,required=True,help='Keep parsed transcripts outside the repository')
    ap.add_argument('--output',type=Path,required=True)
    ap.add_argument('--source-commit',required=True,help='Exact source snapshot SHA')
    ap.add_argument('--changed-only',action='store_true')
    ap.add_argument('--pair',help='Optional targeted review, e.g. 寧々/MEIKO')
    ap.add_argument('--reviewed-evidence',type=Path,help='JSON array of manually reviewed stable evidence IDs')
    ap.add_argument('--top-k',type=int,default=4)
    ap.add_argument('--max-characters',type=int,default=60000)
    args = ap.parse_args()
    if args.top_k<1 or args.max_characters<1 or not re.fullmatch('[0-9a-f]{40}',args.source_commit):
        ap.error('positive budgets and a full 40-character commit SHA are required')
    build(args)
