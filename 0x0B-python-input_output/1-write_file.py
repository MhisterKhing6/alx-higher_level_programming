#!/usr/bin/python3
"""A function that write to file"""


def write_file(filename="", text=""):
    """write_file : write the content of text to fila at file name
    :arg
    :param filename: Path to file to write
    :param text: what to write to filename
    :return: Nothing"""
    with open(filename, "w", encoding='utf-8') as file:
        return file.write(text)