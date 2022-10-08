#!/usr/bin/python3
start = 'a'
count = 1
while count <= ord('z'):
    count = ord(start)
    print(start)
    count += 1
    start = chr(count)
