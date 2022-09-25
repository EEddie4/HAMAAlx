#!/usr/bin/python3
"""A script that
- fetches https://intranet.hbtn.io/status.
- uses urlib package
"""


if __name__ == '__main__':
    import sys
    from urllib.request import urlopen

    url = sys.argv[1]
    with urlopen(url) as response:
        content = dict(response.headers)
        print(content.get("X-Request-Id"))
