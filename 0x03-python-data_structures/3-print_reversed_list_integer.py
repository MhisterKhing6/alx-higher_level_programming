#!/usr/bin/python3

"""Print the content of a list in revers order"""


def print_reversed_list_integer(my_list=[]):
    """"print the vlues in reverse order"""
    for x in range(len(my_list) - 1, -1, -1):

        print("{:d}".format(my_list[x]))
