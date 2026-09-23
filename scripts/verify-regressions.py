"""Compare public live and development markup without exporting visitor sessions."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from hashlib import sha256
from html.parser import HTMLParser
from http.cookiejar import CookieJar
import json
import argparse
from pathlib import Path
import re
import subprocess
from urllib.parse import urljoin, urlsplit, parse_qs
from urllib.request import Request, build_opener, HTTPCookieProcessor

ROOT = Path(__file__).resolve().parents[1]
# Keep the published comparison stable while main receives future releases.
BASELINE_REF = 'baseline/live-wave-1-2026-09-09'
THEME_ID = 142755430600
PATHS = ['/', '/collections/shop-all', '/collections/variety-packs', '/products/lemon-tea',
         '/products/classic-variety', '/products/strawberry-half-half-slim-can',
         '/pages/faq', '/pages/find-in-store', '/pages/contact', '/pages/why-halfday',
         '/pages/our-story', '/pages/hellofresh', '/pages/pto', '/pages/subscribe',
         '/collections/staff-variety-packs']

class Markup(HTMLParser):
    def __init__(self):
        super().__init__(); self.links = set(); self.scripts = set(); self.forms = []; self.product_ids = set()
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'a' and attrs.get('href'): self.links.add(urljoin('https://drinkhalfday.com', attrs['href']))
        if tag == 'script' and attrs.get('src'):
            url = urlsplit(urljoin('https://drinkhalfday.com', attrs['src']))
            # Exclude theme and preview asset paths from the external-loader comparison.
            if '/cdn/shop/t/' not in url.path and 'preview' not in url.path:
                self.scripts.add(url.netloc + url.path)
        if tag == 'form': self.forms.append({'action': attrs.get('action'), 'method': attrs.get('method')})
        if attrs.get('data-product-id'): self.product_ids.add(attrs['data-product-id'])

def fetch(path, development):
    opener = build_opener(HTTPCookieProcessor(CookieJar()))
    query = f'?preview_theme_id={THEME_ID}' if development else ''
    with opener.open(Request('https://drinkhalfday.com' + path + query,
                             headers={'User-Agent': 'Halfday-regression-verification/1.0'}), timeout=40) as response:
        html = response.read().decode('utf-8', 'replace'); status = response.status
    page = Markup(); page.feed(html)
    return html, page, status

def compare(path):
    live_html, live, live_status = fetch(path, False)
    dev_html, dev, dev_status = fetch(path, True)
    theme_match = re.search(r'Shopify\.theme\s*=\s*\{[^}]*"id"\s*:\s*(\d+)', dev_html)
    rendered_theme_id = int(theme_match.group(1)) if theme_match else None
    live_match = re.search(r'Shopify\.theme\s*=\s*\{[^}]*"id"\s*:\s*(\d+)', live_html)
    live_theme_id = int(live_match.group(1)) if live_match else None
    amazon = lambda p: sorted(u for u in p.links if urlsplit(u).hostname in {'amazon.com','www.amazon.com','amzn.to'})
    legacy = lambda page: sorted(u for u in page.links if urlsplit(u).hostname in {'drinkhalfday.com', 'www.drinkhalfday.com', 'halfday-tonics.myshopify.com'} and ('/en-test/' in urlsplit(u).path or 'preview_theme_id' in parse_qs(urlsplit(u).query)))
    markers = ['ShopifyAnalytics', 'web-pixels-manager', 'klaviyo', 'postscript', 'yotpo', 'signifyd', 'acsb', 'locksmith']
    embeds = lambda html: sorted(set(re.findall(r'klaviyo-form-([a-zA-Z0-9]+)', html)))
    return {'path': path, 'live_status': live_status, 'development_status': dev_status,
            'rendered_theme_id': rendered_theme_id, 'rendered_live_theme_id': live_theme_id,
            'development_verified': rendered_theme_id == THEME_ID and live_theme_id is not None and rendered_theme_id != live_theme_id and 'halfday-video.js' in dev_html,
            'liquid_error': 'Liquid error' in dev_html or 'Liquid syntax error' in dev_html,
            'amazon_urls_and_attribution_equal': amazon(live) == amazon(dev),
            'amazon_destination_count': len(amazon(dev)),
            'live_legacy_internal_links': legacy(live), 'development_legacy_internal_links': legacy(dev),
            'removed_external_loaders': sorted(live.scripts - dev.scripts),
            'added_external_loaders': sorted(dev.scripts - live.scripts),
            'integration_markers': {key: {'live': key.lower() in live_html.lower(), 'development': key.lower() in dev_html.lower()} for key in markers},
            'klaviyo_embed_ids_equal': embeds(live_html) == embeds(dev_html),
            'klaviyo_embed_ids': embeds(dev_html),
            'live_forms': live.forms, 'development_forms': dev.forms,
            'removed_product_data_ids': sorted(live.product_ids - dev.product_ids)}

if __name__ == '__main__':
    arguments = argparse.ArgumentParser(description=__doc__)
    arguments.add_argument('--theme-id', type=int, default=THEME_ID, help='Unpublished theme ID to verify')
    arguments.add_argument('--output', type=Path, default=ROOT/'reports/wave-1-regression-markup.json')
    arguments.add_argument('--agentready-embed', choices=['disabled', 'enabled'], default='disabled',
                           help='Expected reviewed theme embed state; shared app output settings need separate verification')
    options = arguments.parse_args()
    THEME_ID = options.theme_id
    with ThreadPoolExecutor(max_workers=3) as pool:
        pages = list(pool.map(compare, PATHS))
    old = subprocess.check_output(['git','show',BASELINE_REF + ':assets/custom.js'], cwd=ROOT).decode()
    new = (ROOT/'assets/custom.js').read_text()
    libraries = {}
    for label, marker in [('jQuery', '/*! jQuery'), ('marquee', '(function(factory)'), ('Swiper', 'var Swiper=function')]:
        if label == 'jQuery':
            old_library = '\n'.join(old.splitlines()[:5]); new_library = '\n'.join(new.splitlines()[:5])
        else:
            old_library = next(line for line in old.splitlines() if line.startswith(marker))
            new_library = next(line for line in new.splitlines() if line.startswith(marker))
        libraries[label] = {'unchanged': old_library == new_library, 'sha256': sha256(new_library.encode()).hexdigest()}
    protected_files = ['snippets/locksmith.liquid', 'assets/product-form.js', 'assets/cart.js', 'assets/cart-drawer.js']
    unchanged = {name: subprocess.check_output(['git','show',BASELINE_REF + ':' + name],cwd=ROOT) == (ROOT/name).read_bytes() for name in protected_files}
    # Isolate the explicitly reviewed Agentready embed change; preserve every other merchant setting.
    original_settings = subprocess.check_output(['git','show',BASELINE_REF + ':config/settings_data.json'],cwd=ROOT).decode()
    current_settings = (ROOT/'config/settings_data.json').read_text()
    original_settings = json.loads(original_settings[original_settings.index('{'):])
    current_settings = json.loads(current_settings[current_settings.index('{'):])
    agentready = current_settings['current']['blocks'].pop('1788854400000000001', None)
    original_settings['current']['blocks'].pop('1788854400000000001', None)
    unchanged['merchant_settings'] = current_settings == original_settings
    unchanged['agentready_embed_matches_expected_state'] = agentready == {
        'type': 'shopify://apps/agentready/blocks/agent-json/019bc449-5f49-7d2d-86cd-f07c7b17ff7b',
        'disabled': options.agentready_embed == 'disabled', 'settings': {}}
    report = {'captured_at':datetime.now(timezone.utc).isoformat(), 'theme_id':THEME_ID, 'baseline_ref':BASELINE_REF,
              'expected_agentready_embed': options.agentready_embed,
              'method':'Separate anonymous cookie jars for public live and development HTML; no forms submitted. Script paths omit query/session values.',
              'limits':'Preserved loaders, attribution URLs, embed IDs and code do not prove receipt of analytics events or conversion attribution. No GA/Ads access; GTM excluded; no purchase/signup events generated.',
              'libraries':libraries, 'unchanged_protected_files':unchanged, 'pages':pages}
    options.output.write_text(json.dumps(report,indent=2)+'\n')
    for p in pages:
        print(p['path'], 'preview',p['development_verified'],'Amazon',p['amazon_urls_and_attribution_equal'], 'loaders_removed',p['removed_external_loaders'],'Klaviyo',p['klaviyo_embed_ids_equal'])
    assert all(x['unchanged'] for x in libraries.values())
    assert all(unchanged.values())
    assert all(not p['removed_external_loaders'] and not p['removed_product_data_ids'] for p in pages)
    assert all(marker['live'] == marker['development'] for p in pages for marker in p['integration_markers'].values())
    assert all(p['live_status']==200 and p['development_status']==200 and p['development_verified'] and not p['liquid_error'] and p['amazon_urls_and_attribution_equal'] and p['klaviyo_embed_ids_equal'] and not p['development_legacy_internal_links'] for p in pages)
