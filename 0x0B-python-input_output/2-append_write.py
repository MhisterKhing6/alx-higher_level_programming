#!/usr/bin/python3
"""A function that write to file"""


def append_write(filename="", text=""):
    """append_write : add to the content of filename
    :arg
    :param filename: Path to file to write
    :param text: what to write to filename
    :return: number of characters added"""
    with open(filename, "a", encoding='utf-8') as file:
        return file.write(text)
