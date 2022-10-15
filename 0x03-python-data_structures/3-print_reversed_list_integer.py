#!/usr/bin/python3

"""Print the content of a list in revers order"""


def print_reversed_list_integer(my_list=[]):
    lenght = len(my_list) - 1
    """"print the vlues in reverse order"""
    while lenght >= 0:
        print("{:d}".format(my_list[lenght]))
        lenght -= 1
