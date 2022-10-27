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
        type(self).typerrr(height, "height")
        type(self).valerr(height, "height")
        type(self).typerrr(width, "width")
        type(self).valerr(width, "width")
        type(self).typerrr(x, "x")
        type(self).valx(x, "x")
        type(self).typerrr(y, "y")
        type(self).valx(y, "y")
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
        type(self).typerrr(wi, "width")
        type(self).valerr(wi, "width")
        self.__width = wi

    @height.setter
    def height(self, wi):

        """set height"""
        type(self).typerrr(wi, "height")
        type(self).valerr(wi, "height")
        self.__height = wi

    @x.setter
    def x(self, wi):
        """set x"""
        type(self).typerrr(wi, "x")
        type(self).valx(wi, "x")
        self.__x = wi

    @y.setter
    def y(self, wi):
        """set y"""
        type(self).typerrr(wi, "y")
        type(self).valx(wi, "y")
        self.__y = wi

    @staticmethod
    def typerrr(value, name):
        """for type erro validation"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))

    @staticmethod
    def valerr(value, name):
        """For value error validation"""
        if value <= 0:
            raise ValueError("{} must be > 0".format(name))

    @staticmethod
    def valx(value, name):
        """For value error validation"""
        if value < 0:
            raise ValueError("{} must be >= 0".format(name))

    def area(self):
        """area: returns the area of the rectangle
            :return : height * width"""
        return self.height * self.width

    def display(self):
        """display: print with '#' the values represented by the triangle"""
        result = '\n' * self.y
        for v in range(self.height):
            result += " "*self.x + "#"*self.width
            if v != self.height - 1:
                result += "\n"
        print(result)

    def __str__(self):
        return "[Rectangle] ({:d}) {:d}/{:d} - {}/{}".\
            format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """
                assigns an argument to each attribute
                """
        lst = (self.id, self.width, self.height, self.x, self.y)
        if args:
            self.id, self.width, self.height, self.x, self.y = \
                args + lst[len(args):len(lst)]
        elif kwargs:
            for (key, value) in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        returns the dictionary representation of a Rectangle.
        """
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width}
