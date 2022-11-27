#!/usr/bin/python3

"""Defines a class and inherired class-checking function."""


def is_kind_of_class(obj, a_class):
    """Check if an object is exactly an instance of a given class.
    Args:
        obj (any): The object yo check.
        a_class (type): The class to match the type of obj
    Returns:
        if obj is an instance or inherited instance of a_class - True.
        otherwise - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
