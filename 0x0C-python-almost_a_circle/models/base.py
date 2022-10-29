#!/usr/bin/python3
import json
from os import path
"""Creates a base class"""


class Base:
    """
    Base: Creates a base class as a template
    :variables
            --nb_objects: A class variable for counting
            id: public instance variable for object identification
    :methods
            __init___: For initializing object
    """
    __nb_objects = 0

    def __init__(self, id=None):

        if id:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dict):
        """to_json_string: Convert object to json representation
        :arg
        :param list_dict: object to represent
        :return: String json representation of list_dict"""
        le = []
        if len(list_dict) != 0:
            le = list_dict
        return json.dumps(le)

    @classmethod
    def save_to_file(cls, list_obj):
        """save_to_file: Save js representation of an object to a file
        :arg
        :param list_obj: contains list of object to convert to a file
        :return: nothing"""
        name = cls.__name__ + ".json"
        with open(name, "w", encoding="utf-8") as fw:
            lwrite = []
            if list_obj:
                for bb in list_obj:
                    lwrite.append(bb.to_dictionary())
            jre = cls.to_json_string(lwrite)
            fw.write(jre)

    @staticmethod
    def from_json_string(json_string):
        """from_jason_string: loads from a json string"""
        if json_string:
            return json.loads(json_string)
        else:
            return []

    @classmethod
    def load_from_file(cls):
        """
        load_from_file: reads an object from a json file
        :return: returns an object from a json file
        """
        name = cls.__name__ + ".json"
        if path.exists(name):
            with open(name, "r", encoding="utf-8") as fre:
                return json.loads(fre)
        else:
            return []

    @classmethod
    def create(cls, **dic):
        """Creates an instance of a class with attribute set
        :arg
        :param dic: values and keys to search
        :returns: a base object"""
        dummy = cls(1, 1)
        dummy.update(**dic)
        return dummy
