#!/usr/bin/python3
import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(55, 44), 99)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -4), -5)

    def test_sub(self):
        self.assertEqual(calc.sub(55, 44), 11)
        self.assertEqual(calc.sub(-1, 1), -2)
        self.assertEqual(calc.sub(-1, -4), 3)

    def test_mul(self):
        self.assertEqual(calc.mul(5, 4), 20)
        self.assertEqual(calc.mul(-1, 1), -1)
        self.assertEqual(calc.mul(-1, -4), 4)

    def test_div(self):
        self.assertEqual(calc.div(25, 5), 5)
        self.assertEqual(calc.div(-1, 1), -1)
        self.assertEqual(calc.div(-4, -1), 4)
        self.assertEqual(calc.div(7, 2), 3.5)
        # method 1 of raising errors
#        self.assertRaises(ValueError, calc.div, 5, 0)
        # method 2 using context manager with
        with self.assertRaises(ValueError):
            calc.div(10, 0)



if __name__ == "__main__":
    unittest.main()
