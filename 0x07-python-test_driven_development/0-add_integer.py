#!/usr/bin/python3
"""Module for an integer define function."""

def add_integer(a, b=98):
    """ adds integers
        Arguments:
        @a: first integer
        @b: second integer default to 98
    """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
