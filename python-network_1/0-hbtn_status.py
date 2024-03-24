#!/usr/bin/python3
"""A script that
- fetches https://intranet.hbtn.io/status and http://0.0.0.0:5050/status
- uses urllib package
"""

import urllib.request

def fetch_status(url):
    with urllib.request.urlopen(url) as res:
        content = res.read()
        print("Body response for {}:".format(url))
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode('utf-8')))
        print()

if __name__ == '__main__':
    urls = ['https://alu-intranet.hbtn.io/status', 'http://0.0.0.0:5050/status']
    for url in urls:
        fetch_status(url)
