#!/usr/bin/python3
"""Check subclass of an object"""


def is_kind_of_class(obj, a_class):
    return issubclass(type(obj), a_class)
