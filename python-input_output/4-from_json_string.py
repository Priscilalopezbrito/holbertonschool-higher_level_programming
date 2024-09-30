#!/usr/bin/python3
"""
From JSON string to Object
"""
import json


def from_json_string(my_str):
    """
    Function that returns an object
    (Python data structure) represented by a JSON string

    Args:
        my_str (str): str

    Return:
        object
    """
    j = json.loads(my_str)
    return j
