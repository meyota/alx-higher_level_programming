#!/usr/bin/python3
"""A module for squares."""


class Square():
    """square class defines size validation"""

    def __init__(self, size=0):
        if (type(size) != int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

