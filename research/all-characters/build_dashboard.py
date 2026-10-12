#!/usr/bin/env python3
"""Build the offline dashboard; no retrieval/inference is performed."""
from pathlib import Path
import json
root=Path(__file__).resolve().parent
data=json.loads((root/'dashboard-data.json').read_text())
assert len(data['records'])==120
payload=json.dumps(data,ensure_ascii=False,separators=(',',':')).replace('<','\\u003c')
(root/'dashboard.html').write_text((root/'dashboard.template.html').read_text().replace('__DATA__',payload))
print('dashboard built:',len(payload),'data characters')
