#!/usr/bin/python3
"""Creates a rectangle class that inherits from Base"""
from base import Base


class Rectangle(Base):
    """Rectangle: inherits from base and use  to implement rectangle
       :attr:
            _width: holds value for width of the rectangle
            _height: holds value for the height of the rectangle
            _x: Value for x cordinate
            _y: value for y cordinate

        :methods:
                __init__ : for initializing
            """
    def __init__(self, width, height, x=0, y=0, id=None):
        """__init__: use for initialization of object
        :arg
        :param width : with of the rectangle
        :param height: height of the rectanle
        :param x : x cordinate
        :param y : y cordinate
        :param id : to identify unique the object
        :return : an object of rectangle
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super(Rectangle, self).__init__(id)

    @property
    def width(self):
        """get width"""
        return self.__width

    @property
    def height(self):
        """get height"""
        return self.__height

    @property
    def x(self):
        """get x"""
        return self.__x

    @property
    def y(self):
        """get y"""
        return self.__y

    @width.setter
    def width(self, wi):
        self.__width = wi

    @height.setter
    def height(self, wi):
        """set height"""
        self.__height = wi

    @x.setter
    def x(self, wi):
        """set x"""
        self.__x = wi

    @y.setter
    def y(self, wi):
        """set y"""
        self.__y = wi
