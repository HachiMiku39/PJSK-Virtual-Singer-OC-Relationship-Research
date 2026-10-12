#!/usr/bin/env python3
"""Check audit coverage, nullable results, nine explanations and fixed-version provenance."""
import argparse, hashlib, json, copy
from refined_scores import compute
from tie_review_gate import require_review
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
 for oc in {r['oc'] for r in d['records']}:
  rr=[r for r in d['records'] if r['oc']==oc]
  for kind in ['growth','emotion']:
   vals=[r[kind]['index'] for r in rr];denom=max(vals) if all(v is not None for v in vals) else None
   if denom==0:denom=None
   for r in rr:
    assert r[kind]['normalization_denominator']==denom
    v=r[kind]['relative_index']
    if denom is None:assert v is None
    else:assert abs(v-100*r[kind]['index']/denom)<1e-8 and 0<=v<=100+1e-8
   if denom is not None:assert abs(max(r[kind]['relative_index'] for r in rr)-100)<1e-8
 for ref in refs.values():
  source=d['source_catalog'][ref['source_id']];assert d['source_commit'] in source['url']
  assert ref['start_line']>=1 and ref['end_line']>=ref['start_line'];assert ref['reviewed_line_runs']
  assert all(ref['start_line']<=s<=e<=ref['end_line'] for s,e in ref['reviewed_line_runs'])
  if corpus_dir:
   b=(corpus_dir/source['path']).read_bytes();assert hashlib.sha256(b).hexdigest()==source['sha256'];assert ref['end_line']<=len(b.decode().splitlines())
 assert len(seen)==120 and len({r['oc'] for r in d['records']})==20
 assert counts['reviewed']==114 and counts['retained']==6
 for oc in {r['oc'] for r in d['records']}:assert len([r for r in d['records'] if r['oc']==oc])==6
 model=json.loads(path.with_name('refinement-judgments.json').read_text());recomputed=compute(copy.deepcopy(d['records']),model['judgments'])
 assert len(model['judgments'])==120 and len({j['pair_id'] for j in model['judgments']})==120
 for row,rebuilt in zip(d['records'],recomputed):
  assert row['refined']==rebuilt['refined']
  j=row['refinement_judgment'];assert j==next(x for x in model['judgments'] if x['pair_id']==row['pair_id'])
  assert j['growth_comparison'] and j['emotion_comparison']
  for k in j['growth_refs']+j['emotion_refs']:assert k in refs
  assert abs(row['refined']['combined_index']-(row['refined']['growth_index']+row['refined']['emotion_index'])/2)<1e-10
 order=json.loads(path.with_name('refined-order-review.json').read_text());mapping={r['pair_id']:r for r in d['records']}
 assert order['unresolved_current_ties']==0 and len(order['pairwise_comparisons'])==80
 for comparison in order['pairwise_comparisons']:
  high=mapping[comparison['higher']];low=mapping[comparison['lower']];metric=comparison['metric']
  assert high['oc']==low['oc']==comparison['oc']
  assert high['refined'][metric+'_index']>low['refined'][metric+'_index']
  assert comparison['dimension_comparison']
  assert all(k in refs for k in comparison['higher_refs']+comparison['lower_refs'])
 tie_count=require_review(d['records'],json.loads(path.with_name('tie-review.json').read_text()),refs)
 print(json.dumps({'pairs':120,'reviewed_coarse_tie_history':tie_count,'current_refined_ties':0,'composite_weight':'1:1',**counts,'fixed_version_refs':len(refs),'checks':'passed'},ensure_ascii=False))

if __name__=='__main__':
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--input',type=Path,default=Path(__file__).with_name('assessments.json'));ap.add_argument('--corpus-dir',type=Path);a=ap.parse_args();validate(a.input,a.corpus_dir)
