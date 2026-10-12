"""Recompute evidence-coded quarter grades and the user's exact 1:1 composite.

All subgrades are supplied by source-linked research judgments, never inferred from
retrieval frequency, rank position, or a target number of distinct scores.
"""
from relative_scores import normalize
from decimal import Decimal, ROUND_HALF_UP

def displayed(value):
 return format(Decimal.from_float(value).quantize(Decimal("0.01"),rounding=ROUND_HALF_UP),".2f")

def compute(records, judgments):
 lookup={j['pair_id']:j for j in judgments};temporary=[]
 for r in records:
  j=lookup[r['pair_id']];qk,qs=j['growth_subgrades'];eq=j['emotion_subgrades']
  assert len(eq)==4 and all(isinstance(q,int) and 0<=q<=3 for q in [qk,qs,*eq])
  K,C,S,T,B=r['growth']['vector'];gv=[K+qk/4,C,S+qs/4,T,B]
  ev=[None if v is None else v+q/4 for v,q in zip(r['emotion']['vector'],eq)]
  assert gv[0]<=4 and gv[2]<=4 and all(v is None or v<=4 for v in ev)
  gi=50*gv[0]/4+15*C/10+20*gv[2]/4+10*T/3+5*B/4;ei=None if None in ev else sum(ev)/16*100
  temporary.append({'pair_id':r['pair_id'],'oc':r['oc'],'growth':{'index':gi},'emotion':{'index':ei}})
  r['refined']={'growth_vector':gv,'emotion_vector':ev,'growth_index_raw':gi,'emotion_index_raw':ei}
 normalize(temporary)
 for r,t in zip(records,temporary):
  f=r['refined'];g=t['growth']['relative_index'];e=t['emotion']['relative_index']
  f.update(growth_index=g,emotion_index=e,combined_index=None if g is None or e is None else (g+e)/2,growth_denominator=t['growth']['normalization_denominator'],emotion_denominator=t['emotion']['normalization_denominator'])
 for oc in dict.fromkeys(r['oc'] for r in records):
  group=[r for r in records if r['oc']==oc]
  for metric in ['growth','emotion','combined']:
   key=metric+'_index';values=[r['refined'][key] for r in group]
   if None in values:
    for r in group:r['refined'][metric+'_rank']=None
    continue
   # An unresolved collision is a research failure, never resolved by an ID/name sort.
   assert len({round(v,8) for v in values})==len(group),('需重新深入评价',oc,metric,values)
   assert len({displayed(v) for v in values})==len(group),('显示两位小数仍同分，需进一步评价',oc,metric,values)
   ordered=sorted(group,key=lambda r:r['refined'][key],reverse=True)
   for rank,r in enumerate(ordered,1):r['refined'][metric+'_rank']=rank
  ordered=sorted(group,key=lambda r:r['refined']['combined_rank'] or 99)
  for i,r in enumerate(ordered):
   current=r['refined']['combined_index'];nxt=ordered[i+1]['refined']['combined_index'] if i+1<len(ordered) else None
   gap=None if current is None or nxt is None else current-nxt
   r['refined']['gap_to_next']=gap
   r['refined']['order_caution']='暂定：综合差距不足2分，子档微调可能换位' if gap is not None and gap<2 else '研究估计；来源有依据，仍需独立复评'
 return records
