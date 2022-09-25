#!/usr/bin/python3
"""A script that
- fetches https://intranet.hbtn.io/status.
- uses urlib package
"""


if __name__ == '__main__':
    from urllib import request

    url = "https://alx-intranet.hbtn.io/status"
    content = request.get(url)
    print("Body response:")
    print("\t - type: {}".format(type(content)))
    print("\t - content: {}".format(content))
