#!/usr/bin/python3
"""A script that
- fetches https://intranet.hbtn.io/status.
- uses urlib package
"""


if __name__ == '__main__':
    from urllib.request import urlopen

    url = "https://alx-intranet.hbtn.io/status"
    with urlopen(url) as response:
        content = response.read()
        print("Body response:")
        print("\t - type: {}".format(type(content.decode('utf-8'))))
        print("\t - content: {}".format(content.decode('utf-8')))
