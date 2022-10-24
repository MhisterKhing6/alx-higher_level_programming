
#!/usr/bin/python3
"""
8-rectangle module
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Represents a rectangle.
    Inherits from BaseGeometry.
    """
    def __init__(self, width, height):
        """
        Initializes an instance.
        Args:
            width: width of the rectangle
            height: height of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """area: Calculate the area
        :return: lenght * width"""
        return self.__width * self.__height

    def __str__(self):
        """
        __str__:Strings representation of the rectangle class
        :return:String representing the class
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
