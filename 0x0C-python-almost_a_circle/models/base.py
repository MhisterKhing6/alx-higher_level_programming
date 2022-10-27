#!/usr/bin/python3
"""Creates a base class"""


class Base:
    """
    Base: Creates a base class as a template
    :variables
            --nb_objects: A class variable for counting
            id: public instance variable for object identification
    :methods
            __init___: For initializing object
    """
    __nb_objects = 0

    def __init__(self, id=None):

        if id:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
