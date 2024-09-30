#!/usr/bin/python3
"""
Append to a file
"""


def append_write(filename="", text=""):
    """
    Append to a file.

    Args:
        filename (str): File name.
        text (str): text

    Returns:
        int: Characters added.
    """
    with open(filename, 'a', encoding="utf-8") as f:
        append_data = f.write(text)
        return append_data
