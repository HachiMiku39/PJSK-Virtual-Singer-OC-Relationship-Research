#!/usr/bin/env python3
"""Build offline dashboard from authoritative assessments; no retrieval/inference."""
from pathlib import Path
import json
from relative_scores import normalize
root=Path(__file__).resolve().parent
source=json.loads((root/'assessments.json').read_text());records=normalize(source['records']);refs=source['audit_refs'];used={v['source_id'] for v in refs.values()}
data={'as_of':source['as_of'],'source_commit':source['source_commit'],'normalization':source['normalization'],'records':[{k:r[k] for k in ['pair_id','oc','unit','vs','vs_key','growth','emotion','audit','tie_review_ids']} for r in records],'refs':refs,'source_catalog':{k:source['source_catalog'][k] for k in sorted(used)},'tie_reviews':json.loads((root/'tie-review.json').read_text()),'palette':json.loads((root/'character-colors.json').read_text())}
assert len(records)==120 and len(data['palette']['entries'])==26
payload=json.dumps(data,ensure_ascii=False,separators=(',',':'))
(root/'dashboard-data.json').write_text(payload+'\n')
(root/'dashboard.html').write_text((root/'dashboard.template.html').read_text().replace('__DATA__',payload.replace('<','\\u003c')))
print('dashboard built:',len(payload),'data characters')
