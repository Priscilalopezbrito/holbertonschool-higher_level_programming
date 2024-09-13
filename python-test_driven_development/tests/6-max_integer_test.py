#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test(self):
        """Test cases"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([4, 4, 4]), 4)
        self.assertEqual(max_integer([2]), 2)
        self.assertEqual(max_integer([]), None)


if __name__ == '__main__':
    unittest.main()
