#!/usr/bin/python3
"""Check subclass of an object"""


def inherits_from(obj, a_class):
    """
    inherits_from: checks if an object inherist from a class
    :param obj: an object to check
    :param a_class: a class for comparison
    :return: true or false is the class match the object
    """
    if type(obj) == a_class:
        return False
    else:
        return issubclass(type(obj), a_class)

