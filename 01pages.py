#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Cкрейпинг/парсинг http://vybary2019.by на чистом Python без зависимостей.
"""

import os
import re
import sys
from urllib.request import urlopen


URL = 'http://vybary2019.by'


def rewrite(filename, content):
    with open(filename, 'w', encoding='utf-8') as fd:
        fd.write(content)
        print('saved %s' % fd.name)


def get_page(url, cachefile, force=False):
    """
    Fetch page and cookie from URL if local cachefile does not exist
    """
    if os.path.exists(cachefile) and not force:
        #print('using cached ' + cachefile + ' (-f to force update)')
        with open(cachefile, encoding='utf-8') as fc:
            cookie = fc.readline().strip()
            return fc.read(), cookie
    else:
        req = urlopen(url)
        output = req.read().decode('utf-8')
        for line in str(req.headers).splitlines():
            if line.startswith('Set-Cookie'):
                cookie = line.split(': ', 1)[1]
                output = cookie+'\n'+output
        rewrite(cachefile, output)
        return output, cookie


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

def parse_regions(content):
  reregion = re.compile('href="(/regions/(\d+).html)">([^<]+)<')
  return [[number, name, URL+path] for path, number, name in reregion.findall(content)]

def get_token(content):
  return re.findall('_token"\s+value="(\w+)"', content)[0]


if __name__ == '__main__':
    force = False
    if '-f' in sys.argv:
        force = True

    content, cookie = get_page(URL + 'regions.html', '01regions_cache', force)

    for number, name, url in parse_regions(content):
       print(f"{number}, {name}, {url}")

    '''
    # next step is fetch, which needs token, laravel_session cookie
    # and list of months
    token = get_token(content)
    # list of months includes current (incomplete) month
    rewrite('002-in-creds.txt', cookie+'\n'+token+'\n'+'\n'.join(months))
    '''
