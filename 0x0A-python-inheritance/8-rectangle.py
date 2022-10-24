#!/usr/bin/python3
"""Creates an empty baseGeo class"""


class BaseGeometry:
    def area(self):
        """Area with exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be  greater than 0".format(name))


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        super(Rectangle, self).__init__()
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height