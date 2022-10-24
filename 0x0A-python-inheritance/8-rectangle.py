#!/usr/bin/python3
"""Creates an rectangle and geom class"""



class BaseGeometry:
    """BaseGeometry: Creates an empty baseGeo class"""
    def area(self):
        """Area with exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        integer_validator: Validate an integer
        :arg
        :param name: name of the integer
        :param value: value
        :return: None upon successful validation else raise exception
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be  greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Rectangle: Create a rectangle class
    """
    def __init__(self, width, height):
        """__init__: Initialize the and validate the rectangle class
        :arg
        :param width: with of the rectangle must be integer and greater than zero
        :param height: height of the rectangle must be integer and greater than zero
        :return: void
        """
        super(Rectangle, self).__init__()
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
