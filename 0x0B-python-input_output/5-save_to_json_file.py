#!/usr/bin/python3
"""A function that creates a json string and write to file"""
import json


def save_to_json_file(my_obj, filename):
    """save_to_json_file : create a json string and save in file
    :arg
    :param my_obj: json object to write to filename
    :param filename: name of the name of json file
    :return: nothing"""
    with open(filename, "w", encoding='utf-8') as file:
        json.dump(my_obj, file)
