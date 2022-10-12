#!/usr/bin/python3
"""Creates a square class and defines it using its base"""


class Square:
    """A square class with bass as only form of definition"""

    def __init__(self, size=0):
        """initialize to size variable"""
        if size != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must b e >= 0")
        else:
            self.__size = size
