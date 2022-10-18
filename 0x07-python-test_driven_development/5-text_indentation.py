#!/usr/bin/python3

def text_indentation(text):
    if type(text) != str:
        raise TypeError("text must be a string")
    for character in text:
        print(character, end="")
        if character == '\n':
            print(" ")
        if character in [':', '.', '?']:
            print()
            print()
