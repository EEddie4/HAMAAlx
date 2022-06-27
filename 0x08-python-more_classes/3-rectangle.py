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
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise TypeError("width must be >= 0")
        self._Rectangle__width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise TypeError("height must be >= 0")
        self._Rectangle__height = height

    @property
    def width(self):
        """ get the current width of the Rectangle"""
        return(self._Rectangle__width)

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise TypeError("width must be >= 0")
        self._Rectangle__width = value

    @property
    def height(self):
        """ get the current height of the Rectangle """
        return(self._Rectangle__height)

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise TypeError("height must be >= 0")
        self._Rectangle__height = value

    ''' calculates area of rectangle object '''
    def area(self):
        return(self._Rectangle__width * self._Rectangle__height)

    ''' calculates perimeter of rectangle object '''
    def perimeter(self):
        if self._Rectangle__width == 0 or self._Rectangle__width == 0:
            return (0)
        else:
            return((self._Rectangle__width + self._Rectangle__height) * 2)

    def __str__(self):
        tab = ""
        if self._Rectangle__height != 0 and self._Rectangle__width != 0:
            for i in range(self._Rectangle__height):
                for j in range(self._Rectangle__width):
                    tab = tab + "#"
                tab = tab + "\n"
        return (tab)
