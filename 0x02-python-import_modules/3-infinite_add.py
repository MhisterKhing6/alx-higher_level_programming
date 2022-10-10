#!/usr/bin/python3if
import sys
if __name__ == "__main__":
    All = 0
    for value in sys.argv[1:]:
        All += int(value)
    print(All)