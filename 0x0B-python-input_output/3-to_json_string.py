#!/usr/bin/python3
"""Defines string to JSOn function."""

import json


def to_json_string(my_obj):
    """returns JSON representation."""
    return json.dumps(my_obj)

