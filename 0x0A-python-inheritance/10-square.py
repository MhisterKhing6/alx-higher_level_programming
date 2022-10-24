#

#!/usr/bin/python3
"""
8-rectangle module
"""
Rectangle =  __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square: Create another geom class for square representation"""
    def __init__(self, size):
        """__init__:initialize square with size
        :arg
        :param size: size of square"""
        super().__init__(size, size)
        self.__size = size

