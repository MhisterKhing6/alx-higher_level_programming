#!/usr/bin/python3
"""Get an element from a list"""


def replace_in_list(my_list, idx, element):
    if (idx >= len(my_list)) or (idx < 0):
        return my_list
    else:
        my_list[idx] = element
        return my_list
