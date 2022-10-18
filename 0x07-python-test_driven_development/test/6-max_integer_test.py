import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxArea(unittest.TestCase):
    def Test_Normal(self):
        self.assertAlmostEquals(max_integer([2, 4, 5, 38, 3]), 38)
        self.assertAlmostEquals(max_integer([2]), 2)
        self.assertAlmostEquals(max_integer([3, 4, 5, 3, 4, 3, 2, 88]), 88)
        self.assertAlmostEquals(max_integer([1, 2, 4, 4]), 4)

    def Test_RASES(self):
        self.assertRaises(TypeError, max_integer, ["how", "sksl"])

    def Test_Empty(self):
        self.assertAlmostEquals(max_integer([]), None)

