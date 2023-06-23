#!/usr/bin/python3
"""
A Python script that:
* fetches https://alx-intranet.hbtn.io/status,
* uses the 'urlib' package.
"""



if __name__ == '__main__':
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        content = res.read()
        print("Body response:")
        print(f"\t- type: {type(content)}")
        print(f"\t- content: {content}")
        print(f"\t- utf8 content: {content.decode('utf-8')}")
