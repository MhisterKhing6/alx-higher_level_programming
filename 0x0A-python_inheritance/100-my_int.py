#!/usr/bin/python3
class MyInt(int):
    def __eq__(self, other):
        return super(MyInt, self).__ne__(other)

    def __ne__(self, other):
        return super(MyInt, self).__eq__(other)
