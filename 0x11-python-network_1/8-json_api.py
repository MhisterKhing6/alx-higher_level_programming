#!/usr/bin/python3
"""  Deal with a json data  """
import requests
import sys
if __name__ == "__main__":
    val = sys.argv[2] if sys.argv[2] else ""
    r = requests.get(sys.argv[1], {'q': val})
    try:
        if r.status_code < 400:
            print('[{}] <{}>'.format(r.json()['id']),
                  r.json()['name'])
    except requests.exceptions.JSONDecodeError as e:
        if r.status_code == 204:
            print("No result")
        else:
            print("Not a valid JSON")
