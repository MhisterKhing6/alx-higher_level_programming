class Square:
    """ defines a function named __init__ """
    def __init__(self, size=0):
        """ if statement """
        if type(size) != int:
            """ raise an error """
            raise TypeError("size must be an integer")
        elif size < 0:
            """ raise an error """
            raise ValueError("size must be >= 0")
        else:
            """ initialize __size of self with size """
            self.__size = size

    def area(self):
        "Returns the current area of the squae"

        return self.__size * self.__size