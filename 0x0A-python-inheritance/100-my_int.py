#!/usr/bin/python3
"""Creates a class for integer representation"""
class MyInt(int):
    """MyInt: An integer class"""
    def __eq__(self, other):
        """__eq__:for equal to comparison
         :arg
         :param other: an iteger to compare to other
         :return true if integer != other, else true"""
        return super(MyInt, self).__ne__(other)

    def __ne__(self, other):
        """__ne__:for not to comparison
                 :arg
                 :param other: an iteger to compare to other
                 :return true if integer == other, else true"""
        return super(MyInt, self).__eq__(other)
