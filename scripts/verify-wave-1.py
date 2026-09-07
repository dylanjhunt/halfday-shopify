"""Read-only HTTP checks of the explicit Wave 1 development preview."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import importlib.util
import json
from pathlib import Path
import sys
from http.cookiejar import CookieJar
from urllib.request import build_opener, HTTPCookieProcessor, Request

sys.dont_write_bytecode = True
root = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('seo_parser', root / 'scripts/audit-seo.py')
parser = importlib.util.module_from_spec(spec)
spec.loader.exec_module(parser)
paths = ['/', '/collections/shop-all', '/collections/variety-packs',
         '/products/lemon-tea', '/products/classic-variety',
         '/products/strawberry-half-half-slim-can', '/pages/faq',
         '/pages/find-in-store', '/pages/popup-testing', '/collections/staff-variety-packs',
         '/blogs/news/kombucha-when-is-the-best-time-to-drink-it',
         '/blogs/news/white-green-tea-shot-vs-green-tea-shot-which-is-the-better-choice',
         '/blogs/news/white-green-tea-shot-vs-green-tea-shots']

def check(path):
    url = 'https://drinkhalfday.com' + path + '?preview_theme_id=142755430600'
    # Shopify redirects away from the preview query after setting an anonymous
    # preview cookie. Preserve it in memory across redirects; never export it.
    opener = build_opener(HTTPCookieProcessor(CookieJar()))
    with opener.open(Request(url, headers={'User-Agent': 'Halfday-development-verification/1.0'}), timeout=30) as response:
        status = response.status
        html = response.read().decode('utf-8', 'replace')
    page = parser.Page()
    page.feed(html)
    return {'path': path, 'status': status, 'development_asset_present': 'halfday-video.js' in html,
            'liquid_error': 'Liquid error' in html or 'Liquid syntax error' in html,
            'title': page.title, 'description': page.description, 'robots': page.robots,
            'canonical': page.canonical, 'structured_data': page.schemas,
            'faq_links': [x for x in page.links if (x.get('href') or '').startswith('#faq_')],
            'remaining_legacy_article_links': [x for x in page.links if x.get('in_main') and (
                (x.get('href') or '').startswith('drinkhalfday.com') or
                (x.get('href') or '').endswith('/pages/shop'))],
            'locator_css': 'find-us.css' in html,
            'high_priority_images': [x for x in page.images if x.get('fetchpriority') == 'high'],
            'public_text': ' '.join(page.main_text).strip()}

if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=3) as pool:
        pages = list(pool.map(check, paths))
    out = {'captured_at': datetime.now(timezone.utc).isoformat(),
           'theme_id': 142755430600, 'method': 'HTTP preview HTML; browser behavior checked separately.',
           'pages': pages}
    (root / 'reports/wave-1-preview-checks.json').write_text(json.dumps(out, indent=2) + '\n')
    for p in pages:
        print(p['path'], p['status'], 'dev:', p['development_asset_present'],
              'liquid_error:', p['liquid_error'], 'description:', bool(p['description']),
              'robots:', p['robots'], 'locator_css:', p['locator_css'])
    assert all(p['status'] == 200 and p['development_asset_present'] and not p['liquid_error'] for p in pages)
    assert all(not p['remaining_legacy_article_links'] for p in pages if '/blogs/' in p['path'])
