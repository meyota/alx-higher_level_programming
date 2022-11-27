#!/usr/bin/python3
"""Unittests for max_integer([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ tests for max_integer([..])."""

    def test_ordered(self):
        """teste for an ordered integers."""
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_none(self):
        """tests empty input."""
        self.assertEqual(max_integer(), None)

    def test_unordered(self):
        """tests unordered list."""
        unordered = [1, 2, 4, 3]
        self.assertEqual(max_integer(unordered), 4)

    def test_neg(self):
        """tests negative."""
        self.assertEqual(max_integer([-1, -2, -3]), -1)

    def test_one_element(self):
        """tests a single element."""
        one_element = [2]
        self.assertEqual(max_integer(one_element), 2)

if __name__ == "__main__":
    unittest.main()
