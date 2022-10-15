#!/usr/bin/python3
"""Get an element from a list"""


def element_at(my_list, idx):
    if (idx >= len(my_list)) or (idx < 0):
        return None
    else:
        return my_list[idx]
