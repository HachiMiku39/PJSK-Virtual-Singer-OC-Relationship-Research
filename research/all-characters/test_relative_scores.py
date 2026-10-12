import unittest
from relative_scores import normalize
class RelativeScoreTests(unittest.TestCase):
 def rows(self):return [{'oc':'A','growth':{'index':x,'vector':[1]},'emotion':{'index':y,'vector':[2]}} for x,y in zip([10,20,40,40,5,0],[80,40,20,80,0,60])]
 def test_two_independent_tied_maxima_and_preserved_raw(self):
  rows=normalize(self.rows());self.assertEqual([r['growth']['relative_index'] for r in rows],[25,50,100,100,12.5,0]);self.assertEqual([r['emotion']['relative_index'] for r in rows],[100,50,25,100,0,75]);self.assertEqual(rows[0]['growth']['index'],10);self.assertEqual(rows[0]['growth']['vector'],[1])
 def test_unknown_cannot_establish_group_maximum(self):
  rows=self.rows();rows[0]['emotion']['index']=None;normalize(rows);self.assertTrue(all(r['emotion']['relative_index'] is None for r in rows));self.assertEqual(rows[1]['emotion']['index'],40);self.assertEqual(rows[2]['growth']['relative_index'],100)
 def test_zero_baseline_stays_unknown(self):
  rows=self.rows()
  for r in rows:r['growth']['index']=0
  normalize(rows);self.assertTrue(all(r['growth']['relative_index'] is None for r in rows));self.assertEqual(rows[0]['emotion']['relative_index'],100)
if __name__=='__main__':unittest.main()
