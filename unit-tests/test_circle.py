!/usr/bin/python3
import unittest
from circle import circle_area
from math import pi


class TestCircleArea(unittest.TestCase):
    def test_area(self):
        """ Test when radius >= 0  """
        self.assertAlmostEqual(circle_area(1), pi)
        self.assertAlmostEqual(circle_area(0), 0)
        self.assertAlmostEqual(circle_area(2.1), pi * 2.1**2)

    def test_values(self):
        """ Raises value error whenever necessary """
        self.assertRaises(ValueError, circle_area, -2)
    
    def test_types(self):
        """ Ensures r is a number """
        self.assertRaises(TypeError, circle_area, 3+5j)
        self.assertRaises(TypeError, circle_area, True)
        self.assertRaises(TypeError, circle_area, "radius")
