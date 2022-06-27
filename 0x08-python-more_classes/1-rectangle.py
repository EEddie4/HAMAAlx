#!/usr/bin/python3
""" Creating a Rectangle class """


class Rectangle:
    """ Creating a Rectangle class """

    def __init__(self, width=0, height=0):
        """ Initialize a new Rectangle
        Args:
            width (int): the width of the new Rectangle
            height (int): the height o the new Rectangle
        """
        self._width = width
        self._height = height

    @property
    def height(self):
        """ get the current height of the Rectangle """
        return(self._height)

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise TypeError("height must be >= 0")
        self._height = value

    @property
    def width(self):
        """ get the current width of the Rectangle"""
        return(self._width)

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise TypeError("width must be >= 0")
        self._width = value
