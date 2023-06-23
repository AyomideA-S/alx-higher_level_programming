#!/usr/bin/python3
"""
A Python script that:
* takes in a letter as a parameter,
* sends POST request to http://0.0.0.0:5000/search_user.
"""

import sys
import requests


if __name__ == "__main__":
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": letter}

    r = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        response = r.json()
        if response == {}:
            print("No result")
        else:
            print(f'[{response.get("id")}] {response.get("name")}')
    except ValueError:
        print("Not a valid JSON")
