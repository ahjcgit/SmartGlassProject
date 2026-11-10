"""Check the public build's links, evidence arithmetic and deployment boundary."""
import csv,json,statistics
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit
ROOT=Path(__file__).resolve().parents[1];out=ROOT/'site'
class Page(HTMLParser):
    def __init__(self):super().__init__();self.ids=set();self.links=[];self.titles=0;self.h1=0
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a:assert a['id'] not in self.ids;self.ids.add(a['id'])
        if tag=='title':self.titles+=1
        if tag=='h1':self.h1+=1
        for attr in ('href','src'):
            if a.get(attr):self.links.append(a[attr])
page=Page();text=(out/'index.html').read_text();page.feed(text)
assert page.h1==page.titles==1
for link in page.links:
    u=urlsplit(link)
    if u.scheme or u.netloc:assert u.scheme=='https';continue
    if not u.path:
        if u.fragment:assert u.fragment in page.ids,link
    else:assert not u.path.startswith('/') and (out/u.path).is_file(),link
assert '/* RESULT_DATA */' not in text and '{{' not in text
s=json.loads((out/'data/results.json').read_text());rows=s['trials'];assert len(rows)==33
assert s['user_annotations']+s['ai_annotations']==s['captured_frames']==229
assert s['ai_annotations_human_verified'] is False
for model in ('nanodet','yolox_s','live_nanodet'):
    trials=[t for t in rows if t['model']==model]
    assert len(trials)==11 and sum(t['frames'] for t in trials)==229
    assert sum(t['visible_frames'] for t in trials)==210 and sum(t['absent_frames'] for t in trials)==19
    for t in trials:
        assert t['fully_reviewed'] and t['capture_complete']
        if t['hit_rate_iou50'] is not None:
            assert 0<=t['hit_rate_iou50']<=1
            hits=t['visible_frames']*t['hit_rate_iou50'];assert abs(hits-round(hits))<1e-8
for model in ('nanodet','yolox_s'):
    assert s['timing'][model]['samples']==229
    for obj in ('sanitizer','toy_motorcycle'):
        rates=[r['hit_rate_iou50'] for r in rows if r['model']==model and r['object_id']==obj]
        assert len(rates)==5 and statistics.mean(rates)==s['condition_means'][model][obj]
assert len(list(csv.DictReader((out/'data/trial-metrics.csv').open())))==33
assert {str(p.relative_to(out)) for p in out.rglob('*') if p.is_file()}=={'index.html','styles.css','app.js','.nojekyll','data/results.json','data/trial-metrics.csv'}
for word in ('password','access_token','refresh_token','192.168.','127.0.0.1','note_text'):
    assert word not in (out/'data/results.json').read_text().lower(),word
print('PASS: local links/anchors, unique headings/IDs, 33 trial-model records, 229-frame counts, hit arithmetic, condition means, CSV coverage, public-file allowlist, no credential/private-content fields.')
