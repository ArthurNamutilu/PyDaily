#!/usr/bin/python3
import unittest
class TestModules(unittest.TestCase):
    def test_addition(self):
        result = 2 + 2
        self.assertEqual(result, 4)
