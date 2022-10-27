"""Creates a square class that inherits from a rectangle"""
from rectangle import Rectangle


class Square(Rectangle):
    """square: Template for a square
    inherits from rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """initializing square class """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({:d}) {:d}/{:d} - {}/{}".\
            format(self.id, self.x, self.y, self.width, self.height)
    @property
    def size(self):
        return self.height

    @size.setter
    def size(self, size):
        self.height(size)
        self.width(size)


def update(self, *args, **kwargs):
    """
    assigns attributes
    """
    lst = (self.id, self.size, self.x, self.y)
    if args:
        self.id, self.size, self.x, self.y = \
            args + lst[len(args):len(lst)]
    elif kwargs:
        for (key, value) in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """
        that returns the dictionary representation of a Square.
        """
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
