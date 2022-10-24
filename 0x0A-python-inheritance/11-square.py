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

    def __str__(self):
        """__str__: Returns the string representation of the class
        :return: A string of the class"""
        return "[Square] {}/{}".format(self.__size, self.__size)

