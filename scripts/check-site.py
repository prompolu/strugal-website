from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
from collections import Counter
ROOT=Path(__file__).resolve().parents[1]/'dist'
class Page(HTMLParser):
 def __init__(self):super().__init__();self.ids=[];self.links=[];self.assets=[];self.labels=set();self.controls=[];self.h1=0;self.images=[]
 def handle_starttag(self,t,a):
  d=dict(a)
  if d.get('id'):self.ids.append(d['id'])
  if t=='a':self.links.append(d.get('href',''))
  if t in ('img','script'):self.assets.append(d.get('src',''))
  if t=='img':self.images.append(d)
  if t=='link' and d.get('rel')=='stylesheet':self.assets.append(d.get('href',''))
  if t=='label' and d.get('for'):self.labels.add(d['for'])
  if t in ('input','select','textarea') and d.get('type')!='hidden':self.controls.append(d)
  if t=='h1':self.h1+=1
pages={}
for p in ROOT.glob('*.html'):
 page=Page();page.feed(p.read_text());pages[p.name]=page
errors=[];links=0
for filename,p in pages.items():
 if p.h1!=1:errors.append(f'{filename}: {p.h1} primary headings')
 for id,count in Counter(p.ids).items():
  if count>1:errors.append(f'{filename}: duplicate id {id}')
 for img in p.images:
  if 'alt' not in img:errors.append(f'{filename}: image without alt')
 for c in p.controls:
  if not(c.get('id') in p.labels or c.get('aria-label') or c.get('aria-labelledby')):errors.append(f'{filename}: unlabelled control {c}')
 for asset in p.assets:
  if asset and not urlsplit(asset).scheme and not(ROOT/unquote(asset)).is_file():errors.append(f'{filename}: missing asset {asset}')
 for href in p.links:
  links+=1;u=urlsplit(href)
  if u.scheme or u.netloc:continue
  target=unquote(u.path) or filename
  if target not in pages:
   if not(ROOT/target).exists():errors.append(f'{filename}: missing destination {href}')
  elif u.fragment and unquote(u.fragment) not in pages[target].ids:errors.append(f'{filename}: missing anchor {href}')
assert not errors,'\n'.join(errors)
assert 'studio-stage' not in (ROOT/'index.html').read_text(),'Rejected 3D section restored'
print(f'PASS: {len(pages)} pages, {links} links, local assets, anchor targets, unique IDs, image alternatives, form labels and one H1 per page.')
