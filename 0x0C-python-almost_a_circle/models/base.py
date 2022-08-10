#!/usr/bin/python3
'''
    Base class for all other classes.
'''
import json
import csv


class Base:
    '''
        manage id attribute in all future classes.
        Arguments:
            @id: id for specfic instance.
    '''

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''
            returns json representation
        '''
        if list_dictionaries is None:
            return '[]'
        return json.dumps(list_dictionaries)

    @staticmethod
    def save_to_file(cls, list_objs):
        '''
            returns dict from a string.
        '''
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)
