#!/usr/bin/python3
"""Defines JSON file writing."""

import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using JSON repr."""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
