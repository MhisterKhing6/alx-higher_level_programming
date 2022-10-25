#!/usr/bin/python3
"""
3-to_json_string module
"""
import json


def from_json_string(my_obj):
    """
    to_json_string - returns  an object representation of json string:
    Args:
        my_obj: string to convert to object
    Return: object
    """
    return json.loads(my_obj)
