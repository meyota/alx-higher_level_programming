#!/usr/bin/python3
"""
    rectangle
"""
from models.base import Base


class Rectangle(Base):
    """Inherits from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        '''
            returning private attribute.
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''
            setting private attribute.
        '''
        self.__width = value

    @property
    def height(self):
        '''
            returning private attribute.
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''
            setting private attribute.
        '''
        self.__height = value
