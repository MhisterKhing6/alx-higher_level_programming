#!/usr/bin/env python3
"""
Fetches a page from https://alx-intranet.hbtn.io/status
"""
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
if __name__ == '__main__':
    req = Request('https://alx-intranet.hbtn.io/status')
    with urlopen(req) as res:
        content = res.read()
        print('Body response:')
        print('\t- type: {}'.format(type(content)))
        print('\t- content: {}'.format(content))
        print('\t- utf8 content: {}'.format(content.decode('utf-8')))
