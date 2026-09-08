"""Summarize local Lighthouse runs without copying request/session payloads."""
from collections import defaultdict
from datetime import datetime, timezone
import json
from pathlib import Path
from statistics import median
import sys
from urllib.parse import urlsplit, parse_qs

source = Path(sys.argv[1])
destination = Path(sys.argv[2])
runs = []
for path in sorted(source.glob('*.json')):
    if not path.name.startswith(('before-', 'after-', 'font-experiment-', 'final-', 'product-font-candidate-')):
        continue
    data = json.loads(path.read_text())
    audits = data['audits']
    requests = audits['network-requests']['details']['items']
    lcp_details = audits.get('lcp-breakdown-insight', {}).get('details', {}).get('items', [])
    node = next((item for item in lcp_details if item.get('type') == 'node'), {})
    cpu = defaultdict(float)
    for item in audits.get('bootup-time', {}).get('details', {}).get('items', []):
        cpu[urlsplit(item.get('url', '')).hostname or 'unattributed'] += item.get('total', 0)
    images = []
    for item in requests:
        url = urlsplit(item.get('url', ''))
        if item.get('resourceType') == 'Image' and '/cdn/shop/files/' in url.path:
            images.append({'file': url.path.rsplit('/', 1)[-1],
                           'width': parse_qs(url.query).get('width', [None])[0],
                           'bytes': item.get('transferSize', 0)})
    runs.append({
        'sample': path.stem, 'lighthouse_version': data['lighthouseVersion'],
        'captured_at': data.get('fetchTime'), 'route': urlsplit(data['finalDisplayedUrl']).path,
        'lcp_ms': audits['largest-contentful-paint']['numericValue'],
        'cls': audits['cumulative-layout-shift']['numericValue'],
        'tbt_ms': audits['total-blocking-time']['numericValue'],
        'fcp_ms': audits['first-contentful-paint']['numericValue'],
        'transfer_bytes': sum(item.get('transferSize', 0) for item in requests),
        'initial_media_bytes': sum(item.get('transferSize', 0) for item in requests if item.get('resourceType') == 'Media'),
        'console_error_audit_pass': audits.get('errors-in-console', {}).get('score') == 1,
        'lcp_selector': node.get('selector'), 'lcp_rect': node.get('boundingRect'),
        'observed_lcp_subparts_ms': next((item.get('items') for item in lcp_details if item.get('type') == 'table'), []),
        'cpu_ms_by_host': dict(sorted(cpu.items(), key=lambda pair: -pair[1])),
        'shopify_images': images,
        'blocking_stylesheets': [urlsplit(item['url']).hostname + urlsplit(item['url']).path
                                for item in audits.get('render-blocking-insight', {}).get('details', {}).get('items', [])
                                if item.get('url')],
        'failed_accessibility_audits': [key for key, value in audits.items()
                                      if value.get('score') == 0 and key in {ref['id'] for ref in data.get('categories', {}).get('accessibility', {}).get('auditRefs', [])}],
    })
groups = []
for stage in ('before', 'after', 'final'):
    for route in sorted({run['route'] for run in runs}):
        selected = [run for run in runs if run['sample'].startswith(stage+'-') and run['route'] == route]
        if not selected:
            continue
        metrics = {key: {'median': median(run[key] for run in selected),
                         'min': min(run[key] for run in selected),
                         'max': max(run[key] for run in selected)}
                   for key in ('lcp_ms', 'cls', 'tbt_ms', 'transfer_bytes', 'initial_media_bytes')}
        groups.append({'stage': stage, 'route': route, 'samples': len(selected), 'metrics': metrics})
destination.write_text(json.dumps({
    'captured_at': datetime.now(timezone.utc).isoformat(),
    'baseline_commit': 'ab0afbc', 'theme_id': 142755430600,
    'method': 'Sequential fresh-profile mobile Lighthouse, same development theme, no app/request blocking. Two baseline runs per route. Final runs retain the original font loader, with collection video deferral and responsive image improvements. Product-font-candidate runs are the rejected product-only font experiment. The after stage is an earlier broad-font experiment, not the retained final candidate; isolated font-only runs are also retained. Final home/collection performance captures precede the subsequent semantic heading and desktop announcement-link inheritance refinements, which do not change mobile frame geometry or resource loading.',
    'limits': 'Local simulated lab results, not field Core Web Vitals. Observed LCP subparts use a different timing model from simulated LCP and must not be added to it. Third-party and workstation variation remain. No browser navigation or parallel benchmarking during measurement batches.',
    'groups': groups, 'runs': runs,
}, indent=2)+'\n')
for group in groups:
    print(group['stage'], group['route'], group['samples'],
          'LCP', round(group['metrics']['lcp_ms']['median']),
          'CLS', round(group['metrics']['cls']['median'], 6),
          'bytes', round(group['metrics']['transfer_bytes']['median']))
