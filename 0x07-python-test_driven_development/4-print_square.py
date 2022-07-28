#!/usr/bin/python3
"""Module that prints a square"""


def print_square(size):
    """Print a square with # character.

    Args:
        @size: size of the square
    Raises:
        TypeError: if size is not an integer.
        ValueError: if size is < 0.
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if (size < 0):
        raise ValueError("size must be >= 0")
    if size == 0:
        return
    for i in range(size):
        for j in range(size):
            print('#', end="")
        print()
