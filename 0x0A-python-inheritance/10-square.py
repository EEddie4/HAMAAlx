#!/usr/bin/python3
"""
Contains the class BaseGemetry
"""

BaseGeometry = __import__('9-rectangle').BaseGeometry


class Square(BaseGeometry):
    """ The class empty"""

    def __init__(self, size):
        """raises an exception when called"""
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        return "[Rectangle] {:d}/{:d}".format(self.__size, self.__size)

    def area(self):
        return (self.__size ** 2)
