#!/usr/bin/python3

def uppercase(str):
    for c in str:
        if (ord(c) <= ord('z')) and (ord(c) >= ord('a')):
            print(chr(ord(c) - 32), end="")
        else:
            print(c, end="")
    print()
uppercase('I love you hun you are my true love and i love you plenty babe indeed you touch me in defferent ways possible')