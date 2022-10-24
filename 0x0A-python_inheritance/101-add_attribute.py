#!/usr/bin/python3

def add_attribute(a, b, c):
    if b in dir(a) or type(a) is str:
        raise TypeError("can't add new attribute")
    a.__dict__[b] = c
