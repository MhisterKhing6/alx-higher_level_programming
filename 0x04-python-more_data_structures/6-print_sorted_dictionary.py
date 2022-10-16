#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    ke = list(a_dictionary.keys())
    ke.sort()
    for key in ke:
        print("{:s}: {}".format(key, a_dictionary[key]))
