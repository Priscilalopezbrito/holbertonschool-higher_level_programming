#!/usr/bin/python3
"""
Save Object to a file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file, using
    a JSON representation.

    Args:
        my_obj (str): obj
        filename (str): File name
    """
    with open(filename, 'w', encoding="utf-8") as f:
        j = json.dumps(my_obj)
        f.write(j)
