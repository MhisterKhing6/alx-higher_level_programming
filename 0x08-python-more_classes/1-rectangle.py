#!/usr/bin/python3
"""Defines an empty class called Rectangle"""


class Rectangle:
    """Empty definition of rectangle"""

    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width

    @ property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, a):
        if type(a) != int:
            raise TypeError("width must be an integer")
        if a < 0:
            raise ValueError("width must be >= 0")
        self.__width = a

    @height.setter
    def height(self, a):
        if type(a) != int:
            raise TypeError("height must be an integer")
        if a < 0:
            raise ValueError("height must be >= 0")
        self.__height = a
