#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    my_dic = {a: b*2 for (a, b) in a_dictionary.items()}
    return my_dic
