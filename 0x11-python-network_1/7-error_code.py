#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL and
displays the body of the response.
If the HTTP status code is greater than or equal to 400,
print: Error code: followed by the value of the HTTP status
"""

import requests
import sys

if __name__ == "__main__":
    res = requests.get(sys.argv[1])
    if res.status_code >= 400:
        print("Error code: {}".format(res.status_code))
    else:
        print(res.text)
