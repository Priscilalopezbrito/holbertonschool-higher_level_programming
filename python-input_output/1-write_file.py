#!/usr/bin/python3
"""
Write to a file
"""


def write_file(filename="", text=""):
    """
    Write to a file.

    Args:
        filename (str): File name.
        text (str): text
    """
    with open(filename, 'w', encoding="utf-8") as f:
        write_data = f.write(text)
        return write_data
