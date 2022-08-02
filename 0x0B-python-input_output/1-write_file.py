#!/usr/bin/python3

"""Defines file writing."""


def write_file(filename="", text=""):
    """Write a string to UTF8 text file.
    Args:
        filename (str): the name of a file to write.
        text (str): the text to write to the file.
    Returns:
        The number of character written
    """
    with open(filename, "w", encoding="UTF8") as f:
        return f.write(text)
