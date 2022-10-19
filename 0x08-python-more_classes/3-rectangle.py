#!/usr/bin/python3
"""Defines an empty class called Rectangle"""


class Rectangle:
    """Empty definition of rectangle"""

    def __init__(self, width=0, height=0):
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
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

    def area(self):
        return self.height * self.width

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return 2*self.width + 2*self.height

    def __str__(self):
        strrep = ""
        if self.height == 0 or self.width == 0:
            return ""
        for i in range(self.height):
            if i == self.height - 1:
                strrep += "#"*self.width
            else:

                strrep += "#"*self.width + '\n'
        return strrep
