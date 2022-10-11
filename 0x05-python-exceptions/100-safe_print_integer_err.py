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
value = "School"
has_been_print = safe_print_integer_err(value)
if not has_been_print:
    print("{} is not an integer".format(value))
