#!/usr/bin/python3
"""
To JSON string
"""
import json


def to_json_string(my_obj):
    """
    Function that returns the JSON representation
    of an object (string)

    Args:
        my_obj (): obj

    Return:
        string
    """
    j = json.dumps(my_obj)
    return j
