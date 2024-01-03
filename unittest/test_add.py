import unittest
from add import add


class MyTestCases(unittest.TestCase):
    """ test class """
    def add_test(self):
        self.assertEqual(add(3, 97), 100)
        