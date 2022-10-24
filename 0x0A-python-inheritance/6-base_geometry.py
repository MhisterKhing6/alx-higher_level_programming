#!/usr/bin/python3
"""Creates an empty baseGeo class"""


class BaseGeometry:
    def area(self):
        """Area with exception"""
        raise Exception("area() is not implemented")
