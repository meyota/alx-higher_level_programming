#!/usr/bin/python3
"""Defines JSON to object."""

import json


def from_json_string(my_str):
    """returns JSON representation."""
    return json.loads(my_str)
