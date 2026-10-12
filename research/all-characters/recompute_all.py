#!/usr/bin/env python3
"""Validate proposed codes, formulas and approval-aware results without inventing missing inputs."""
import argparse
import hashlib
import json
from pathlib import Path
from compact_assessments import resolve_ref


def validate(path, corpus_dir=None):
    data=json.loads(path.read_text(encoding='utf-8'))
    rows=data['records'];seen=set();counts={'trial_existing':0,'pending':0}
    for row in rows:
        key=(row['oc'],row['vs_key'])
        assert key not in seen, key
        seen.add(key)
        g=row['growth'];K,C,S,T,B=g['vector'];n=g['n_strong_lines_proposed']
        assert all(isinstance(x,int) for x in (K,C,S,T,B,n)),key
        assert 0<=K<=4 and 0<=S<=4 and 0<=T<=3 and 0<=B<=4 and n>=0,key
        assert C==[0,4,7,9,10][min(n,4)],key
        gi=50*K/4+15*C/10+20*S/4+10*T/3+5*B/4
        assert abs(gi-g['index'])<1e-8,key
        e=row['emotion'];assert len(e['vector'])==4
        assert all(isinstance(v,int) and 0<=v<=4 for v in e['vector']),key
        assert abs(100*sum(e['vector'])/16-e['index'])<1e-8,key
        existing=row['growth_input_approval']=='既有一歌试评'
        if existing:
            assert row['approved_growth_index']==g['index']
            assert row['approved_emotion_index']==e['index']
            counts['trial_existing']+=1
        else:
            assert row['approved_growth_index'] is None,key
            assert row['approved_emotion_index'] is None,key
            counts['pending']+=1
        refs=[x['source'] for x in row['evidence']['historical_facts']]
        refs+=row['evidence']['manually_read_focus']
        refs+=[x['source'] for x in row['evidence']['emotion_candidates']]
        refs=[resolve_ref(data,ref) for ref in refs]
        for ref in refs:
            assert ref['start_line']>=1 and ref['end_line']>=ref['start_line']
            assert data['source_commit'] in ref['url']
            if corpus_dir:
                p=corpus_dir/ref['path'];raw=p.read_bytes()
                assert hashlib.sha256(raw).hexdigest()==ref['sha256'],ref['path']
                assert ref['end_line']<=len(raw.decode('utf-8').splitlines()),ref['path']
    assert len(seen)==120 and len({x[0] for x in seen})==20
    for oc in {x[0] for x in seen}:
        assert len([x for x in seen if x[0]==oc])==6
    print(json.dumps({'pairs':len(seen),'existing_trial_pairs':counts['trial_existing'],
                      'unapproved_pairs':counts['pending'],'formula_and_provenance_checks':'passed'},ensure_ascii=False))


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input',type=Path,default=Path(__file__).with_name('assessments.json'))
    parser.add_argument('--corpus-dir',type=Path)
    args=parser.parse_args();validate(args.input,args.corpus_dir)
