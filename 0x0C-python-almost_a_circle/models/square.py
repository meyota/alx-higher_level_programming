#!/usr/bin/python3
'''
    class Square
'''

from models.rectangle import Rectangle


class Square(Rectangle):
    '''Inherits from rectangle.'''

    def __init__(self, size, x=0, y=0, id=None):
        '''
            Initialization a square.
        '''
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        '''
            square size getter.
        '''
        return self.width

    @size.setter
    def size(self, value):
        '''
            square size setter.
        '''
        self.width = value
        self.height = value

    def __str__(self):
        '''
            returns formatted representation.
        '''
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id,
                                                         self.x,
                                                         self.y,
                                                         self.width)

    def update(self, *args, **kwargs):
        '''update square'''
        if len(args):
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
        else:
            for k, v in kwargs.items():
                if hasattr(self, k) is True:
                    setattr(self, k, v)
