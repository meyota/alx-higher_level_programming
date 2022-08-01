#!/usr/bin/python3

"""Defines a Rectangle subclass Square."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size):
        """Defines attributes"""
        self.integer_validator("size", size)
        self.__size =size

    def area(self):
        """calulates area of square"""
        return self.__size * self.__size

    def __str__(self):
        """Representaion of a square"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
