#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    sys.path.append("add_0")
    import add_0 as func
    a = 1
    b = 2

    print("{} + {} = {}".format(a, b, func.add(a, b)))
