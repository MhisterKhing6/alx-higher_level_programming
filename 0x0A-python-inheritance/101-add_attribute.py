#!/usr/bin/python3
"""Check to see if an attribute can be added to a class"""
def add_attribute(a, b, c):
    """add_attribute: Add an attribute b of value c to class
    :arg
    :param a:An object for attribute to be added
    :param b: name of attribute
    :param c:  value of attribute
    :return None upon success else exception"""
    if b in dir(a) or type(a) is str:
        raise TypeError("can't add new attribute")
    a.__dict__[b] = c
