import unittest,json,copy
from pathlib import Path
from refined_scores import compute
class RefinedScoringTest(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  root=Path(__file__).parent;cls.records=json.loads((root/'assessments.json').read_text())['records'];cls.judgments=json.loads((root/'refinement-judgments.json').read_text())['judgments']
 def test_formula_and_complete_distinct_orders_preserve_coarse(self):
  rows=copy.deepcopy(self.records);old=[copy.deepcopy([r['growth'],r['emotion']]) for r in rows];compute(rows,self.judgments)
  for r,prior in zip(rows,old):
   self.assertEqual([r['growth'],r['emotion']],prior);f=r['refined'];self.assertEqual(f['combined_index_raw'],(f['growth_index']+f['emotion_index'])/2)
  for oc in {r['oc'] for r in rows}:
   rr=[r for r in rows if r['oc']==oc]
   for m in ['growth','emotion','combined']:
    self.assertEqual({r['refined'][m+'_rank'] for r in rr},set(range(1,7)));self.assertEqual(len({round(r['refined'][m+'_index'],2) for r in rr}),6)
   self.assertAlmostEqual(max(r['refined']['growth_index'] for r in rr),100,places=12);self.assertAlmostEqual(max(r['refined']['emotion_index'] for r in rr),100,places=12);self.assertEqual(max(r['refined']['combined_index'] for r in rr),100)
   mean_order=sorted(rr,key=lambda r:r['refined']['combined_index_raw'],reverse=True);self.assertEqual([r['refined']['combined_rank'] for r in mean_order],list(range(1,7)))
 def test_different_component_leaders_still_have_composite_100(self):
  rr=[r for r in self.records if r['oc']=='花里实乃理'];self.assertLess(max(r['refined']['combined_index_raw'] for r in rr),100);self.assertEqual(max(r['refined']['combined_index'] for r in rr),100)
 def test_missing_metric_keeps_entire_composite_group_unknown(self):
  rows=copy.deepcopy(self.records);rows[0]['emotion']['vector'][0]=None;compute(rows,self.judgments)
  for r in rows[:6]:self.assertIsNone(r['refined']['emotion_index']);self.assertIsNone(r['refined']['combined_index_raw']);self.assertIsNone(r['refined']['combined_denominator']);self.assertIsNone(r['refined']['combined_index']);self.assertIsNone(r['refined']['combined_rank'])
 def test_unresolved_collision_fails_instead_of_id_tiebreak(self):
  rows=copy.deepcopy(self.records);rows[1]['growth']['vector']=rows[2]['growth']['vector'];js=copy.deepcopy(self.judgments);js[1]['growth_subgrades']=js[2]['growth_subgrades']
  with self.assertRaises(AssertionError):compute(rows,js)
if __name__=='__main__':unittest.main()
