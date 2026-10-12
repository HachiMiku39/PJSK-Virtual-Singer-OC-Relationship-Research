import unittest
from tie_review_gate import require_review,tied_groups
class TieReviewGateTest(unittest.TestCase):
 def setUp(self):
  self.rows=[{'pair_id':p,'oc':'A','growth':{'index':50.,'vector':[2]},'emotion':{'index':i,'vector':[2]}} for p,i in [('R',25.),('L',50.)]]
  self.item={'id':'T1','status':'深入评价完成','comparison':'实际剧情作用不同，同档边界无证据拉开','conclusion':'保留并列','input':{'oc':'A','metric':'growth','raw_index':50.,'pairs':['R','L']},'members':[{'pair_id':p,'vector_after_review':[2],'reviewed_story_refs':['ref']} for p in ['R','L']]}
  self.review={'reviews':[self.item],'final_tied_group_count':1,'unreviewed_final_ties':0}
 def test_only_within_same_oc_and_metric(self):
  self.assertEqual(len(tied_groups(self.rows)),1)
  self.assertEqual(require_review(self.rows,self.review,{'ref':{}}),1)
 def test_new_tie_is_rejected(self):
  self.rows[0]['emotion']['index']=50.
  with self.assertRaises(AssertionError):require_review(self.rows,self.review,{'ref':{}})
 def test_changed_vector_requires_new_comparison(self):
  self.rows[0]['growth']['vector']=[3]
  with self.assertRaises(AssertionError):require_review(self.rows,self.review,{'ref':{}})
if __name__=='__main__':unittest.main()
