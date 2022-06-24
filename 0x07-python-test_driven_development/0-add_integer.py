#!/usr/bin/python3
"""
this projet alx
"""


def add_integer(a, b=98):
    """
    this function return sum a and b
    """

    test1 = type(a) == int or type(a) == float
    test2 = type(b) == int or type(b) == float
    if test1 and test2:
        return (a + b)
    elif test1:
        raise ValueError("b must be an integer")
    elif test2:
        raise ValueError("a must be an integer")
