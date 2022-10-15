#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    newList = my_list.copy()
    if (idx >= len(my_list)) or (idx < 0):
        return newList
    else:
        newList[idx] = element
        return newList
