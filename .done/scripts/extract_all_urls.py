#!/usr/bin/env python3

import xml.etree.ElementTree as ET
import pathlib

ns = {'sm': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
sitemap = pathlib.Path('public/sitemap.xml')
if not sitemap.exists():
    print('No sitemap.xml found')
    exit(0)

urls = []
for url in ET.parse(sitemap).getroot().findall('sm:url', ns):
    loc = url.find('sm:loc', ns)
    if loc is not None:
        urls.append(loc.text)

with open('changed_urls.txt', 'w') as f:
    f.write('\n'.join(urls))
