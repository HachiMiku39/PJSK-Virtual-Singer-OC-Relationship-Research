"""Require a source-linked comparative review for every within-OC score tie."""
from collections import defaultdict

def tied_groups(records):
 buckets=defaultdict(list)
 for row in records:
  for metric in ('growth','emotion'):
   value=row[metric]['index']
   if value is not None:buckets[(row['oc'],metric,round(value,8))].append(row['pair_id'])
 return [(key,sorted(ids)) for key,ids in buckets.items() if len(ids)>1]

def require_review(records,review,refs):
 rows={r['pair_id']:r for r in records};covered={}
 for item in review['reviews']:
  assert item['status']=='深入评价完成' and item['comparison'].strip() and item['conclusion'].strip()
  g=item['input'];members={m['pair_id']:m for m in item['members']}
  assert set(members)==set(g['pairs'])
  for m in members.values():assert m['reviewed_story_refs'] and all(k in refs for k in m['reviewed_story_refs'])
  key=(g['oc'],g['metric'],round(g['raw_index'],8),tuple(sorted(g['pairs'])))
  # Superseded groups remain as history; only matching current vectors can cover a current tie.
  if all(m['vector_after_review']==rows[pid][g['metric']]['vector'] for pid,m in members.items()):covered[key]=item['id']
 final=[]
 for (oc,metric,score),ids in tied_groups(records):
  key=(oc,metric,score,tuple(ids));assert key in covered,('必须深入评价的新同分或过期评价',key)
  final.append(covered[key])
 assert len(final)==review['final_tied_group_count']
 assert review['unreviewed_final_ties']==0
 return len(final)
