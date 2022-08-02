#!/usr/bin/python3

"""Define text append."""


def append_write(filename="", text=""):
    """Append string to the end of UTF8 text file.

    Arrgs:
        filename (str): The name of the file to append to.
        text (str): The string to append to the file.
    returns:
        number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
