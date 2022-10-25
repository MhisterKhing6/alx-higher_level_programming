#!/usr/bin/python3
"""A function that creates a json string and write to file"""
import json


def load_from_json_file(filename):
    """load_from_json_file : create an object from a json file
    :arg
    :param filename: file for json object
    :return: nothing"""
    with open(filename, "r", encoding='utf-8') as file:
        return json.load(file)
