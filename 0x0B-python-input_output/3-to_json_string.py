#!/usr/bin/python3
import json
"""convert to json string implementation"""


def to_json_string(my_obj):
    """to_json_string : convert object to json object
    :arg
    :param my_obj : object to convert to json implementation
    :return: jason serilization of the object"""
    return json.dumps(my_obj)
