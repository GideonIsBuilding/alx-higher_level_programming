#!/usr/bin/python3
""" Module that contains a function that returns the number of lines
    of a text file
"""


def write_file(filename="", text=""):
    """ Function that reads from a file and prints its number of lines

    Args:
        filename: filename

    Raises
        Exception: when the file can be opened

    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
