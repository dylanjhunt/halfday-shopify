"""Bounded, read-only crawl of public sitemap URLs. No auth or form submissions."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import HTTPError
from xml.etree import ElementTree as ET
import hashlib
import json

BASE = 'https://drinkhalfday.com'
NS = {'s': 'http://www.sitemaps.org/schemas/sitemap/0.9'}

def request(url):
    try:
        response = urlopen(Request(url, headers={'User-Agent': 'Halfday-read-only-site-audit/2.0'}), timeout=30)
    except HTTPError as error:
        response = error
    with response as r:
        return r.status, r.url, dict(r.headers), r.read().decode('utf-8', 'replace')

class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title = ''; self.description = None; self.canonical = None; self.robots = []
        self.headings = []; self.schemas = []; self.links = []; self.images = []
        self.main_text = []; self.article_text = []; self.in_main = False; self.in_article = False
        self.in_title = False; self.script = False; self.style = False; self.ld = False; self.ld_text = ''
        self.heading = None; self.anchor = None
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'main': self.in_main = True
        if tag == 'article': self.in_article = True
        if tag == 'title': self.in_title = True
        if tag == 'style': self.style = True
        if tag in ['h1','h2','h3']: self.heading = {'tag':tag, 'text':'', 'in_main':self.in_main}
        if tag == 'meta' and a.get('name','').lower() == 'description': self.description = a.get('content')
        if tag == 'meta' and a.get('name','').lower() in ['robots','googlebot']: self.robots.append(a.get('content'))
        if tag == 'link' and a.get('rel') == 'canonical': self.canonical = a.get('href')
        if tag == 'a': self.anchor = {'href':a.get('href'), 'text':'', 'in_main':self.in_main}
        if tag == 'img': self.images.append({k:a.get(k) for k in ['src','alt','loading','fetchpriority','sizes','width','height']})
        if tag == 'script':
            self.script = True; self.ld = a.get('type') == 'application/ld+json'; self.ld_text = ''
    def handle_endtag(self,tag):
        if tag == 'main': self.in_main = False
        if tag == 'article': self.in_article = False
        if tag == 'title': self.in_title = False
        if tag == 'style': self.style = False
        if self.heading and tag == self.heading['tag']:
            self.headings.append(self.heading); self.heading = None
        if tag == 'a' and self.anchor:
            self.links.append(self.anchor); self.anchor = None
        if tag == 'script':
            if self.ld:
                try: self.schemas.append(json.loads(self.ld_text))
                except ValueError: self.schemas.append({'parse_error':True})
            self.script = False; self.ld = False
    def handle_data(self,data):
        if self.in_title: self.title += data
        if self.ld: self.ld_text += data
        if self.script or self.style: return
        if self.heading: self.heading['text'] += data
        if self.anchor: self.anchor['text'] += data
        if data.strip():
            if self.in_main: self.main_text.append(data.strip())
            if self.in_article: self.article_text.append(data.strip())

def crawl(url):
    try:
        status, final, headers, html = request(url)
        p = Page(); p.feed(html)
        main = ' '.join(p.main_text); article = ' '.join(p.article_text)
        return dict(url=url, status=status, final_url=final, title=p.title.strip(),
                    description=p.description, canonical=p.canonical, robots=p.robots,
                    x_robots_tag=headers.get('X-Robots-Tag'), headings=p.headings,
                    structured_data=p.schemas, links=p.links, images=p.images,
                    main_text=main, article_text=article,
                    main_hash=hashlib.sha256(main.encode()).hexdigest(),
                    shogun_marker='shogun' in html.lower())
    except Exception as e:
        return {'url':url,'error':str(e)}

if __name__ == '__main__':
    _, _, _, xml = request(BASE+'/sitemap.xml')
    maps = []
    for loc in ET.fromstring(xml).findall('s:sitemap/s:loc', NS):
        if not loc.text.startswith(BASE+'/'): continue
        _, _, _, child = request(loc.text)
        urls = [n.text for n in ET.fromstring(child).findall('s:url/s:loc', NS)]
        maps.append({'sitemap':loc.text,'urls':urls})
    urls = sorted({u for m in maps for u in m['urls'] if u.startswith(BASE+'/') and not u.endswith('.md')})
    assert len(urls) <= 100, 'Review crawl bounds before expanding past 100 URLs.'
    with ThreadPoolExecutor(max_workers=4) as pool:
        pages = list(pool.map(crawl, urls))
    _, _, _, robots = request(BASE+'/robots.txt')
    out = {'captured_at':datetime.now(timezone.utc).isoformat(),
           'method':'Public HTTP sitemap crawl, no auth; rendered visibility/indexing is not inferred from HTTP alone.',
           'sitemaps':maps, 'robots_txt':robots, 'pages':pages}
    dest = Path(__file__).resolve().parents[1]/'reports/seo-crawl-2026-09-07.json'
    dest.write_text(json.dumps(out,indent=2)+'\n')
    print('Crawled',len(pages),'URLs;',sum('error' in p for p in pages),'fetch errors;',dest)
    for p in pages:
        print(p['url'].removeprefix(BASE),p.get('status',p.get('error')),repr(p.get('title')), 'description:',bool(p.get('description')),'robots:',p.get('robots'))
