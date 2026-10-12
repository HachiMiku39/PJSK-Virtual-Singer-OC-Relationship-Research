#!/usr/bin/env python3
"""Check audit coverage, nullable results, nine explanations and fixed-version provenance."""
import argparse, hashlib, json
from pathlib import Path

def validate(path, corpus_dir=None):
 d=json.loads(path.read_text());seen=set();counts={'retained':0,'reviewed':0,'unknown_emotion_dimensions':0,'complete_emotion_indices':0};refs=d['audit_refs']
 for row in d['records']:
  key=row['pair_id'];assert key not in seen;seen.add(key)
  g=row['growth'];K,C,S,T,B=g['vector'];n=g['n_strong_lines_reviewed']
  assert all(isinstance(x,int) for x in [K,C,S,T,B,n]);assert 0<=K<=4 and 0<=S<=4 and 0<=T<=3 and 0<=B<=4 and n>=0
  assert C==[0,4,7,9,10][min(n,4)];gi=50*K/4+15*C/10+20*S/4+10*T/3+5*B/4
  assert abs(gi-g['index'])<1e-8 and abs(gi-row['approved_growth_index'])<1e-8
  e=row['emotion'];v=e['vector'];assert len(v)==4 and all(x is None or isinstance(x,int) and 0<=x<=4 for x in v)
  unknown=v.count(None);counts['unknown_emotion_dimensions']+=unknown
  if unknown:assert e['index'] is None and row['approved_emotion_index'] is None
  else:
   assert abs(sum(v)/16*100-e['index'])<1e-8;assert e['index']==row['approved_emotion_index'];counts['complete_emotion_indices']+=1
  known=sum(x for x in v if x is not None);assert e['index_interval']==[known/16*100,(known+4*unknown)/16*100]
  a=row['audit'];assert len(a['growth_notes'])==5 and len(a['emotion_notes'])==4 and all(a['growth_notes']+a['emotion_notes'])
  assert n==len(a['independent_lines']);assert len(a['growth_dimension_refs'])==5 and len(a['emotion_dimension_refs'])==4
  for note_refs in a['growth_dimension_refs']+a['emotion_dimension_refs']:assert note_refs and all(x in refs for x in note_refs)
  assert all(x in refs for x in a['rejected'])
  counts['retained' if a['status']=='既有一歌试评沿用' else 'reviewed']+=1
 for ref in refs.values():
  source=d['source_catalog'][ref['source_id']];assert d['source_commit'] in source['url']
  assert ref['start_line']>=1 and ref['end_line']>=ref['start_line'];assert ref['reviewed_line_runs']
  assert all(ref['start_line']<=s<=e<=ref['end_line'] for s,e in ref['reviewed_line_runs'])
  if corpus_dir:
   b=(corpus_dir/source['path']).read_bytes();assert hashlib.sha256(b).hexdigest()==source['sha256'];assert ref['end_line']<=len(b.decode().splitlines())
 assert len(seen)==120 and len({r['oc'] for r in d['records']})==20
 assert counts['reviewed']==114 and counts['retained']==6
 for oc in {r['oc'] for r in d['records']}:assert len([r for r in d['records'] if r['oc']==oc])==6
 print(json.dumps({'pairs':120,**counts,'fixed_version_refs':len(refs),'checks':'passed'},ensure_ascii=False))

if __name__=='__main__':
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--input',type=Path,default=Path(__file__).with_name('assessments.json'));ap.add_argument('--corpus-dir',type=Path);a=ap.parse_args();validate(a.input,a.corpus_dir)
