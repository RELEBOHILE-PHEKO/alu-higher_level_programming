#!/usr/bin/python3

"""A script that

- fetches content from two URLs simultaneously.
- uses urllib package

"""

import urllib.request

if __name__ == '__main__':
    urls = ['https://alu-intranet.hbtn.io/status', 'http://0.0.0.0:5050/status']

    for url in urls:
        try:
            with urllib.request.urlopen(url) as res:
                content = res.read()
                print("Body response for {}:".format(url))
                print("\t- type: {}".format(type(content)))
                print("\t- content: {}".format(content))
                print("\t- utf8 content: {}".format(content.decode('utf-8')))
                print()
        except urllib.error.URLError as e:
            print("Error fetching {}: {}".format(url, e.reason))
