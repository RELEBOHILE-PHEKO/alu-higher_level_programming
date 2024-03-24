#!/usr/bin/python3
"""This script retrieves the status of the intranet.hbtn.io
website using the requests library
and prints details about the response content"""

import requests

if __name__ == '__main__':
    url = 'https://intranet.hbtn.io/status'
    if url.startswith('https://'):
        url = "https://alu-intranet.hbtn.io/status"
    res = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(res.text)))
    print("\t- content: {}".format(res.text))
