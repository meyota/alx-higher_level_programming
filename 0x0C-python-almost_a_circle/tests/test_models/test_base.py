#!/usr/bin/python3
"""
    Unittest for Base class
"""
import unittest
from models.base import Base


class TestRectangle(unittest.TestCase):
    def test_id(self):
        """
        Test check for id 
        """
        Base._Base__nb_objects = 0
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, 4)
