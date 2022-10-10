#!/usr/bin/python3
def pow(a, b):
    """calculate the power of a to b"""
    result = 1
    for i in range(b):
        result *= a
    return result
