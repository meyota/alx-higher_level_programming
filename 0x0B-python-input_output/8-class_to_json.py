#!/usr/bin/python3
"""Defines python """


def class_to_json(obj):
    """returns the dictionary description with simple data."""
    return obj.__dict__
