#!/usr/bin/python3
"""
Create object from a JSON file
"""
import json


def load_from_json_file(filename):
    """
    Creates an Object from a “JSON file".

    Args:
        filename (str): File name

    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
