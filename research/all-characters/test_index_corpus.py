"""Regression checks for incremental retrieval, target boundaries and budget gates."""
import argparse
import contextlib
import io
import json
import tempfile
import unittest
from pathlib import Path
from index_corpus import build, identity, named_target


class RetrievalTests(unittest.TestCase):
    def test_target_and_roleplay_boundaries(self):
        self.assertFalse(named_target('リンゴとトランポリンが好き','Rin'))
        self.assertTrue(named_target('リン、ありがとう','Rin'))
        self.assertEqual(identity('女の子(寧々)'), (None,None))
        self.assertEqual(identity('寧々'), ('oc','寧々'))
        self.assertEqual(identity('ミク(Leo/need)'), ('vs','Miku'))

    def test_cache_edit_delete_and_budget(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            corpus = root/'story_jp'/'event';corpus.mkdir(parents=True)
            p = corpus/'001.txt'
            p.write_text('ミク: 話してみて\n一歌: ミク、聞いてくれてありがとう\n',encoding='utf-8')
            q = corpus/'002.txt';q.write_text('リン: こんにちは\n一歌: リン、ありがとう\n',encoding='utf-8')
            args = argparse.Namespace(corpus_dir=root/'story_jp',cache_dir=root/'cache',
                output=root/'out.json',source_commit='a'*40,changed_only=False,
                pair=None,top_k=4,max_characters=10000)
            def run():
                with contextlib.redirect_stdout(io.StringIO()):build(args)
                return json.loads(args.output.read_text(encoding='utf-8'))
            first = run();self.assertEqual(first['stats']['parsed_files'],2)
            second = run();self.assertEqual(second['stats']['parsed_files'],0)
            self.assertEqual(first['evidence'],second['evidence'])
            reviewed = root/'reviewed.json';reviewed.write_text(json.dumps(list(first['evidence'])),encoding='utf-8')
            args.reviewed_evidence=reviewed
            self.assertEqual(run()['stats']['unique_windows'],0)
            args.reviewed_evidence=None
            args.changed_only=True
            self.assertEqual(run()['stats']['unique_windows'],0)
            p.write_text(p.read_text(encoding='utf-8')+'一歌: ミクのおかげで気づいた\n',encoding='utf-8')
            changed = run();self.assertEqual(changed['stats']['parsed_files'],1)
            self.assertEqual(changed['changed_paths'],['story_jp/event/001.txt'])
            self.assertTrue(changed['evidence'])
            q.unlink();self.assertEqual(run()['removed_paths'],['story_jp/event/002.txt'])
            args.changed_only=False;args.max_characters=1
            tiny=run();self.assertEqual(tiny['stats']['unique_windows'],0)
            self.assertLessEqual(tiny['stats']['evidence_payload_characters'],1)


if __name__=='__main__':unittest.main()
