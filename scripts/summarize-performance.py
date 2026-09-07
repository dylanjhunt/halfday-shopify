"""Summarize local Lighthouse runs without retaining cookies, query tokens or screenshots."""
from datetime import datetime, timezone
from pathlib import Path
from statistics import median
from urllib.parse import urlsplit, urlunsplit
import json
import sys

raw_dir = Path(sys.argv[1] if len(sys.argv) > 1 else '/private/tmp/halfday-lighthouse-20260907')
groups = ['home', 'pdp', 'collection', 'home-no-video', 'home-no-signifyd']
metric_ids = ['first-contentful-paint','largest-contentful-paint','total-blocking-time',
              'cumulative-layout-shift','speed-index','total-byte-weight']

def clean_url(value):
    u = urlsplit(value)
    return urlunsplit((u.scheme,u.netloc,u.path,'',''))

runs = []
for group in groups:
    for i in range(1,4):
        name = f'{group}-{i}'
        data = json.loads((raw_dir/(name+'.json')).read_text())
        assert not data.get('runtimeError'), (name,data.get('runtimeError'))
        a = data['audits']
        row = dict(run=name, group=group, captured_at=data['fetchTime'],
                   url=data['finalDisplayedUrl'], lighthouse_version=data['lighthouseVersion'],
                   environment=data['environment'], config=data['configSettings'], warnings=data['runWarnings'],
                   scores={k:v['score'] for k,v in data['categories'].items()},
                   metrics={k:a[k].get('numericValue') for k in metric_ids},
                   observed_metrics=a['metrics']['details']['items'][0],
                   resource_summary=a['resource-summary']['details']['items'])
        row['third_parties'] = [{k:e.get(k) for k in ['entity','transferSize','mainThreadTime']}
                               for e in a['third-parties-insight']['details']['items']]
        row['network'] = [{**{k:r.get(k) for k in ['resourceType','transferSize','resourceSize','priority','statusCode']},
                           'url':clean_url(r['url'])} for r in a['network-requests']['details']['items']
                          if r.get('url','').startswith('https://')]
        for key in ['lcp-discovery-insight','lcp-breakdown-insight']:
            # Selectors and timing suffice; HTML snippets can contain session-specific URLs.
            details = []
            for item in a.get(key,{}).get('details',{}).get('items',[]):
                if item.get('type')=='node': details.append({'type':'node','selector':item.get('selector'),'boundingRect':item.get('boundingRect')})
                else: details.append(item)
            row[key] = details
        for key in ['image-delivery-insight','unused-javascript','unused-css-rules']:
            row[key] = {'display':a.get(key,{}).get('displayValue'), 'items':[
                {**{k:r.get(k) for k in ['totalBytes','wastedBytes']},'url':clean_url(r.get('url',''))}
                for r in a.get(key,{}).get('details',{}).get('items',[]) if r.get('url')]}
        runs.append(row)

summary = {}
for group in groups:
    members = [r for r in runs if r['group']==group]
    summary[group] = {'n':len(members),'performance_score_median':median(r['scores']['performance'] for r in members),
                      'metrics':{key:{'median':median(r['metrics'][key] for r in members),
                                      'min':min(r['metrics'][key] for r in members),
                                      'max':max(r['metrics'][key] for r in members)} for key in metric_ids}}
out = {'summarized_at':datetime.now(timezone.utc).isoformat(),
       'method':'15 sequential Lighthouse 13.4.1 mobile simulated-throttling runs, fresh temporary Chrome profiles. Three runs per group. Request blocking is diagnostic only, not a shipped change or feature-equivalent replacement.',
       'excluded_run':'home-no-video-or-signifyd: the combined pattern did not block the intended resources; excluded from comparisons.',
       'groups':summary,'runs':runs}
dest = Path(__file__).resolve().parents[1]/'reports/performance-audit-2026-09-07.json'
dest.write_text(json.dumps(out,indent=2)+'\n')
print('Saved',len(runs),'sanitized runs to',dest)
