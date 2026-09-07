"""Read-only, bounded public storefront snapshot. No cookies or Admin API access."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import HTTPError
import json
import re

BASE = 'https://drinkhalfday.com'
PATHS = ['/', '/collections/shop-all', '/products/lemon-tea', '/products/green-tea',
         '/products/classic-variety', '/en-test/products/lemon-iced-tea',
         '/pages/find-in-store', '/pages/faq', '/pages/our-story',
         '/pages/why-halfday', '/pages/contact', '/robots.txt', '/sitemap.xml']

class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title = ''; self.description = None; self.canonical = None
        self.h1 = []; self.scripts = []; self.styles = []; self.images = []
        self.links = []; self.schemas = []; self.text = []
        self.in_title = False; self.in_h1 = False; self.script = False
        self.ld = False; self.ld_text = ''; self.style = False
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'title': self.in_title = True
        if tag == 'h1': self.in_h1 = True
        if tag == 'style': self.style = True
        if tag == 'meta' and a.get('name') == 'description': self.description = a.get('content')
        if tag == 'link' and a.get('rel') == 'canonical': self.canonical = a.get('href')
        if tag == 'link' and a.get('rel') == 'stylesheet': self.styles.append(a.get('href'))
        if tag == 'a' and a.get('href'): self.links.append(a['href'])
        if tag == 'img': self.images.append({k:a.get(k) for k in ['src','alt','width','height','loading','fetchpriority']})
        if tag == 'script':
            self.script = True; self.ld = a.get('type') == 'application/ld+json'; self.ld_text = ''
            if a.get('src'): self.scripts.append(a['src'])
    def handle_endtag(self, tag):
        if tag == 'title': self.in_title = False
        if tag == 'h1': self.in_h1 = False
        if tag == 'style': self.style = False
        if tag == 'script':
            if self.ld:
                try: self.schemas.append(json.loads(self.ld_text))
                except ValueError: self.schemas.append({'parse_error': True})
            self.script = False; self.ld = False
    def handle_data(self, data):
        if self.in_title: self.title += data
        if self.in_h1 and data.strip(): self.h1.append(data.strip())
        if self.ld: self.ld_text += data
        if not self.script and not self.style and data.strip(): self.text.append(data.strip())

def fetch(path):
    req = Request(BASE + path, headers={'User-Agent':'Halfday-read-only-site-audit/1.0'})
    try:
        with urlopen(req, timeout=30) as r:
            raw = r.read(); status = r.status; final = r.url
    except HTTPError as e:
        raw = e.read(); status = e.code; final = e.url
    except Exception as e:
        return {'path': path, 'error': str(e)}
    html = raw.decode('utf-8', errors='replace')
    out = {'path':path, 'status':status, 'final_url':final, 'html_bytes':len(raw)}
    if path.endswith(('.xml','.txt')):
        out['body'] = html
    else:
        p = Page(); p.feed(html)
        out.update(title=p.title.strip(), description=p.description, canonical=p.canonical,
                   h1=p.h1, scripts=p.scripts, styles=p.styles, images=p.images,
                   links=sorted(set(p.links)), structured_data=p.schemas,
                   text=' '.join(p.text), shogun_marker=bool(re.search('shogun',html,re.I)))
    return out

if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=4) as pool: pages = list(pool.map(fetch, PATHS))
    output = {'captured_at':datetime.now(timezone.utc).isoformat(),
              'method':'Public HTTP, no browser rendering; bytes are HTML body size, not transfer size or performance scores.', 'pages':pages}
    dest = Path(__file__).resolve().parents[1] / 'reports/public-storefront-baseline.json'
    dest.write_text(json.dumps(output,indent=2)+'\n')
    for p in pages:
        print(p['path'],p.get('status',p.get('error')),p.get('html_bytes'),
              'scripts',len(p.get('scripts',[])), 'h1',p.get('h1'),
              'sold out',p.get('text','').lower().count('sold out'))
