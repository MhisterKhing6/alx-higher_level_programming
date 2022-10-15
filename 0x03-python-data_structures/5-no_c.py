#!/usr/bin/python3
def no_c(my_string):
    newString = ""
    for character in my_string:
        if character == 'c':
            pass
        elif character == 'C':
            pass
        else:
            newString += character
    return newString
