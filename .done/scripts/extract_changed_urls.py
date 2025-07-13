#!/usr/bin/env python3

import os
import datetime as dt
import xml.etree.ElementTree as ET
import pathlib
import sys

cutoff = dt.datetime.utcnow() - dt.timedelta(hours=int(os.getenv('CHANGE_WINDOW_HOURS', '24')))
ns = {'sm': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
sitemap = pathlib.Path('public/sitemap.xml')

if not sitemap.exists():
    print('No sitemap.xml found')
    sys.exit(0)

urls = []
for url in ET.parse(sitemap).getroot().findall('sm:url', ns):
    lm = url.find('sm:lastmod', ns)
    if lm is None:
        continue
    try:
        ts = dt.datetime.fromisoformat(lm.text.replace('Z', '+00:00')).replace(tzinfo=None)
    except ValueError:
        continue
    if ts >= cutoff:
        loc = url.find('sm:loc', ns)
        if loc is not None:
            urls.append(loc.text)

with open('changed_urls.txt', 'w') as f:
    f.write('\n'.join(urls))
