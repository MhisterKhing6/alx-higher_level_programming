#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except TypeError as t:
        print(t, file=sys.stderr)
    except ValueError as v:
        print(v, file=sys.stderr)
        return False
