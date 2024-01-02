import unittest
from ongeza import ongeza


class MyTestCases(unittest.TestCase):
    def test_add(self):
          self.assertEqual(ongeza(7, 3), 10)
