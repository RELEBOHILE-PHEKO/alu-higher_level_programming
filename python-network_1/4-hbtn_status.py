#!/usr/bin/python3
"""Fetches https://alu-intranet.hbtn.io/status."""
import requests


if __name__ == "__main__":
    r = requests.get("https://alu-intranet.hbtn.io/status")
    expected_content = "Custom status"
    print("Body response:\n\t- type: {}\n\t- content: {}".format(type(r.text), r.text))
    print("Received output matches the expected output." if r.text.strip() == expected_content else "Received output does not match the expected output.")
