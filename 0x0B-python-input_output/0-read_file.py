#!/usr/bin/python3
"""A function that reads from file and print it to stdout"""


def read_file(filename=""):
    """read_file : Reads the content of a file to stdout
    :arg
    :param filename: Path to file for readig
    :return: Nothing"""
    with open(filename, encoding='utf-8') as file:
        for line in file:
            print(line, end='')
