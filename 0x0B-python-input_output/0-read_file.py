#!/usr/bin/python3

"""Defines read file"""


def read_file(filename=""):
    """read function"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
