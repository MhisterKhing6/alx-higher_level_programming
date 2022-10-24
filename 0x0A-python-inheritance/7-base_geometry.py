#!/usr/bin/python3
"""Creates an empty baseGeo class"""


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
