#!/usr/bin/env python3
"""Normalize display indices within each OC and metric; preserve raw indices and codes."""
def normalize(records):
 for oc in dict.fromkeys(r['oc'] for r in records):
  rows=[r for r in records if r['oc']==oc]
  for metric in ['growth','emotion']:
   values=[r[metric]['index'] for r in rows]
   denominator=max(values) if len(values)==6 and all(v is not None for v in values) else None
   if denominator==0:denominator=None
   for r in rows:
    r[metric]['normalization_denominator']=denominator
    r[metric]['relative_index']=100*r[metric]['index']/denominator if denominator is not None else None
 return records
