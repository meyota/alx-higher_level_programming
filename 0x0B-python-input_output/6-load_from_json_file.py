#!/usr/bin/python3
"""Defines JSON file reading."""

import json


def load_from_json_file(filename):
    """creat python object from JSON file."""
    with open(filename) as f:
        return json.load(f)
