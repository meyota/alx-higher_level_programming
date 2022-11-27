#!/usr/bin/python3
"""
Test for the Square class
"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """Testing Square
    """

    def tearDown(self):
        """Tears down obj count
        """

        Base._Base__nb_objects = 0
        self.assertEqual(Base._Base__nb_objects, 0)
