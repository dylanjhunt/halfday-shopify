"""Verify public sitemap metadata on the development theme; retain no page bodies."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import argparse
import importlib.util
import json
from pathlib import Path
import re
from urllib.parse import urlsplit
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
def module(name, filename):
    spec = importlib.util.spec_from_file_location(name, ROOT/'scripts'/filename)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result

seo = module('seo', 'audit-seo.py')
regression = module('regression', 'verify-regressions.py')

def verify(url):
    path = urlsplit(url).path
    try:
        html, _, status = regression.fetch(path, True)
        page = seo.Page(); page.feed(html)
        theme = re.search(r'Shopify\.theme\s*=\s*\{[^}]*"id"\s*:\s*(\d+)', html)
        return {'path': path, 'status': status,
                'preview_verified': bool(theme and int(theme.group(1)) == regression.THEME_ID),
                'title': page.title.strip(), 'description_present': bool(page.description),
                'canonical': page.canonical, 'robots': page.robots,
                'h1': [h['text'].strip() for h in page.headings if h['tag'] == 'h1'],
                'schema_parse_errors': sum(bool(s.get('parse_error')) for s in page.schemas if isinstance(s, dict)),
                'liquid_error': 'Liquid error' in html or 'Liquid syntax error' in html,
                'legacy_internal_links': sorted({link['href'] for link in page.links
                    if link.get('href') and '/en-test/' in link['href']})}
    except Exception as error:
        return {'path': path, 'error': str(error)}

if __name__ == '__main__':
    arguments = argparse.ArgumentParser(description=__doc__)
    arguments.add_argument('--retry-errors', action='store_true', help='Recheck only failed URLs in the existing report after a cooldown')
    options = arguments.parse_args()
    destination = ROOT/'reports/wave-1-seo-closure.json'
    if options.retry_errors:
        report = json.loads(destination.read_text())
        failures = [p for p in report['pages'] if p.get('error')]
        report.setdefault('retry_history', []).append({'at': datetime.now(timezone.utc).isoformat(), 'previous_failures': failures})
        for index, page in enumerate(report['pages']):
            if page.get('error'):
                report['pages'][index] = verify(seo.BASE+page['path'])
        destination.write_text(json.dumps(report, indent=2)+'\n')
        print('Rechecked', len(failures), 'previous failures;', sum(bool(p.get('error')) for p in report['pages']), 'remaining')
        assert all(p.get('status') == 200 and p.get('preview_verified') and not p.get('liquid_error') and not p.get('schema_parse_errors') and not p.get('legacy_internal_links') for p in report['pages'])
        raise SystemExit(0)
    status, _, _, xml = seo.request(seo.BASE+'/sitemap.xml')
    assert status == 200
    urls = set()
    for loc in ET.fromstring(xml).findall('s:sitemap/s:loc', seo.NS):
        if not loc.text.startswith(seo.BASE+'/'): continue
        status, _, _, child = seo.request(loc.text)
        assert status == 200
        urls.update(n.text for n in ET.fromstring(child).findall('s:url/s:loc', seo.NS)
                    if n.text.startswith(seo.BASE+'/') and not n.text.endswith('.md'))
    assert 0 < len(urls) <= 100, 'Review crawl scope before expanding.'
    with ThreadPoolExecutor(max_workers=2) as pool:
        pages = list(pool.map(verify, sorted(urls)))
    report = {'captured_at': datetime.now(timezone.utc).isoformat(), 'theme_id': regression.THEME_ID,
              'method': 'Fresh public sitemap discovery; separate anonymous development-preview cookie jar per URL. No page bodies or customer data retained; no forms submitted.',
              'limits': 'Technical HTML checks, not search indexing, ranking, AEO traffic or editorial claim approval. Utility URLs may intentionally be noindex or access controlled.',
              'pages': pages}
    destination.write_text(json.dumps(report, indent=2)+'\n')
    print('Crawled', len(pages), 'public sitemap URLs')
    for page in pages:
        if page.get('error') or not page.get('description_present') or len(page.get('h1', [])) != 1 or page.get('robots') or page.get('schema_parse_errors') or page.get('legacy_internal_links'):
            print(json.dumps(page))
    assert all(p.get('status') == 200 and p.get('preview_verified') and not p.get('liquid_error') and not p.get('schema_parse_errors') and not p.get('legacy_internal_links') for p in pages)
