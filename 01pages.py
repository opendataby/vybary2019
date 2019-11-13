#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Cкрейпинг/парсинг http://vybary2019.by на чистом Python без зависимостей.
"""

import csv
import os
import re
import sys
from urllib.request import urlopen


URL = 'http://vybary2019.by'


def write_csv(filename, data, header):
    with open(filename, 'w', encoding='utf-8') as fd:
        print('writing %s' % fd.name)
        writer = csv.writer(fd, dialect='unix')
        writer.writerow(header)
        for row in data:
            writer.writerow(row)


def get_page(url, cachefile, force=False):
    """
    Fetch page and cookie from URL if local cachefile does not exist
    """
    if os.path.exists(cachefile) and not force:
        print('using cached ' + cachefile + ' (-f to force update)')
        with open(cachefile, 'rb') as fc:
            return fc.read().decode('utf-8')
    else:
        req = urlopen(url)
        output = req.read()
        print(f'caching {url} to {cachefile}')
        with open(cachefile, 'wb') as cw:
            cw.write(output)
        return output.decode('utf-8')


def get_months(content):
  """ Get (parse) list of months from content """
  remonth = re.compile('name="month-filter" value="(\d\d\d\d-\d\d-\d\d)"')
  return remonth.findall(content)

def calc_months(curdate):
  """ Calculate months up to curdate from hardcoded date """
  hardcoded = '2015-11-01'
  date = [int(i) for i in hardcoded.split('-')]
  res = []
  while date <= [int(i) for i in curdate.split('-')]:
    res.append('{:04d}-{:02d}-{:02d}'.format(*date))
    y, date[1] = divmod(date[1]+1, 13)
    if y:
      date[1] = 1
      date[0] += 1
  return res


def parse_region_list(content):
  reregion = re.compile('href="(/regions/(\d+).html)">([^<]+)<')
  return [[number, name, URL+path] for path, number, name in reregion.findall(content)]


def parse_region_data(content):
  reppl = re.compile('Количество избирателей</strong>([^<]+)<')
  reloc = re.compile('тельной комиссии</strong>([^<]+)<')
  recon = re.compile('Контакты:</strong>([^<]+)<')

  ppl = reppl.findall(content)[0]  # get first (and the only) match
  # strip all markup from ' – 65 522.\n'
  ppl = ppl.replace(' ', '').strip('\r\n.–')

  loc = reloc.findall(content)[0]
  loc = loc.replace('\r\n', ' ').strip('\r\n:. ')

  con = recon.findall(content)[0]
  con = re.sub('\s+', ' ', con).strip()

  return ppl, loc, con


if __name__ == '__main__':
    force = False
    if '-f' in sys.argv:
        force = True

    # directories cache/ and dataset/ needs to be present

    content = get_page(URL + '/regions.html', 'cache/regions.html', force)

    # number, name, url
    regions = parse_region_list(content)
    header = 'number name url'.split()

    for idx, (number, name, url) in enumerate(regions):
        content = get_page(url, f'cache/region{number}.html', force)
        ppl, loc, con = parse_region_data(content)
        # insert people field after the name
        nameidx = header.index('name')
        regions[idx].insert(nameidx+1, ppl)
        regions[idx].insert(nameidx+2, loc)
        regions[idx].insert(nameidx+3, con)
    header.insert(nameidx+1, 'people')
    header.insert(nameidx+2, 'location')
    header.insert(nameidx+3, 'contact')

    write_csv('dataset/regions.csv', regions, header)

    '''
    # next step is fetch, which needs token, laravel_session cookie
    # and list of months
    token = get_token(content)
    # list of months includes current (incomplete) month
    rewrite('002-in-creds.txt', cookie+'\n'+token+'\n'+'\n'.join(months))
    '''
