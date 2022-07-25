#!/usr/bin/python3

"""A module for working with Rectangle."""


class Rectangle:
    """Defines a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a rectangle.
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrives the width of this Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrives the height of this Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return 2 * (self.__width + self.height)

    def __str__(self):
        """Return the printable representation of the rectangle.
        Represents the rectangle with # character.
        """

        if self.__width == 0 or self.__height == 0:
            return ''
        else:
            res = list(map(
                lambda x: '#' * self.__width + '\n' * (x != self.__height -1),
                range(self.__height)))
            return ''.join(res)

    def __repr__(self):
        """Return the string representation of the rectangle."""
        return 'Rectangle({:d}, {:d})'.format(self.__width, self.__height)
