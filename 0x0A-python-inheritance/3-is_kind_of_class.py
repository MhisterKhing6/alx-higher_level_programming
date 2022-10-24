#!/usr/bin/python3
"""Check subclass of an object"""


def is_kind_of_class(obj, a_class):
    """
        is_kind_of_class - check if an object is a subb class of an instance of a given class.
        Args:
            obj: The object to check.
            a_class: The class to match the type of obj to.
        Returns: If obj is exactly an instance of a_class - True,
                Otherwise - False.
        """
    return issubclass(type(obj), a_class)
