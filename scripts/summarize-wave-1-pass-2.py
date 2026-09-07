"""Export performance evidence without raw browser/session URLs or screenshots.

Usage: python3 scripts/summarize-wave-1-pass-2.py /path/to/lighthouse-json-directory
"""
from collections import defaultdict
from datetime import datetime, timezone
import json
from pathlib import Path
from statistics import median
import sys

root = Path(__file__).resolve().parents[1]
source = Path(sys.argv[1])

def owner(url):
    if '/assets/custom.js' in url:
        return 'Theme custom.js'
    for token, name in [('signifyd.com', 'Signifyd'), ('acsbapp.com', 'accessiBe'),
                        ('klaviyo.com', 'Klaviyo'), ('yotpo.com', 'Yotpo'),
                        ('postscript.io', 'Postscript'), ('shogun', 'Shogun')]:
        if token in url.lower():
            return name
    return None

def result(path):
    data = json.loads(path.read_text())
    audits = data['audits']
    resources = audits['network-requests']['details']['items']
    costs = defaultdict(float)
    for item in audits['bootup-time']['details']['items']:
        group = owner(item['url'])
        if group:
            costs[group] += item['total']
    metrics = {key: audits[audit]['numericValue'] for key, audit in {
        'lcp_ms': 'largest-contentful-paint', 'fcp_ms': 'first-contentful-paint',
        'tbt_ms': 'total-blocking-time', 'cls': 'cumulative-layout-shift',
        'transfer_bytes': 'total-byte-weight', 'main_thread_ms': 'mainthread-work-breakdown'}.items()}
    metrics['initial_media_bytes'] = sum(item['transferSize'] for item in resources if item.get('resourceType') == 'Media')
    for key, category in data['categories'].items():
        metrics[key + '_score'] = category['score'] * 100
    metrics['theme_custom_js_ms'] = costs['Theme custom.js']
    return {'capture': path.name, 'captured_at': data['fetchTime'], 'metrics': metrics,
            'reported_main_thread_attribution_ms': {key: round(value, 2) for key, value in costs.items()},
            'preview_video_asset_present': any('halfday-video.js' in item['url'] for item in resources)}

groups = {}
for prefix, label in [('before', 'previous_checkpoint'), ('after', 'intermediate_before_header_repair'),
                      ('final', 'delivered_theme_during_browser_qa'), ('quiet', 'delivered_theme_without_concurrent_navigation')]:
    runs = [result(path) for path in sorted(source.glob(prefix + '-*.json'))]
    if runs:
        groups[label] = {'runs': runs, 'median': {key: median(run['metrics'][key] for run in runs) for key in runs[0]['metrics']}}
report = {'captured_at': datetime.now(timezone.utc).isoformat(), 'theme_id': 142755430600,
          'method': 'Lighthouse 13.4.1, default simulated mobile throttling, a separate CLI Chrome launch per run, same development preview URL and categories: performance, accessibility, SEO.',
          'caveats': [
              'Shopify redirects the preview URL and sets an anonymous preview cookie. All captures checked for the development video asset; raw cookies and request URLs are not exported.',
              'The delivered-theme QA batch showed a large paint regression. Additional runs without concurrent preview navigation investigate that variability, not erase the earlier results. Cause is unproven; do not claim consistent LCP improvement or field CWV improvement.',
              'Main-thread attribution is from the Lighthouse bootup-time table, which omits small entries. It is CPU work attributed to a source, not elapsed page-load time or an uninstall saving guarantee.',
              'No app settings changed. Third-party execution and the development preview make results variable. Initial media bytes do not measure post-scroll media consumption.'
          ], 'groups': groups}
(root / 'reports/wave-1-performance-pass-2.json').write_text(json.dumps(report, indent=2) + '\n')
for label, group in groups.items():
    print(label, {key: round(value, 2) for key, value in group['median'].items()})
