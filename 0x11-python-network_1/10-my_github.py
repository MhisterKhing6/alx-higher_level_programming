#!/usr/bin/python3
"""Display the user id from github"""
import requests
from requests.auth import HTTPBasicAuth
import sys
if __name__ == "__main__":
    r = requests.get('https://api.github.com/user',
                     auth=HTTPBasicAuth(sys.argv[1],
                                        sys.argv[2]))
    if r.status_code < 400:
        try:
            db = r.json()
            print(db.get('id', "None"))
        except ValueError as err:
            pass
