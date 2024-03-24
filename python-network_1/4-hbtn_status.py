#!/usr/bin/python3
"""
This script retrieves the status of the intranet.hbtn.io
website using the requests library
and prints details about the response content
"""

import requests

if _name_ == '_main_':
    url = 'https://intranet.hbtn.io/status'
    if url.startswith('https://'):
        url = "https://alu-intranet.hbtn.io/status"
    res = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(res.text)))
    print("\t- content: {}".format(res.text))
