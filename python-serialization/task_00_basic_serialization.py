#!/usr/bin/env python3
import pickle
"""
Basic serialization module that adds the
functionality to serialize a Python dictionary
to a JSON file and deserialize the JSON file
to recreate the Python Dictionary.
"""


def serialize_and_save_to_file(data, filename):
    """
    Function serialize_and_save_to_file
    """
    with open(filename, 'wb') as f:
        pickle.dump(data, f)


def load_and_deserialize(filename):
    """
    Function load_and_deserialize
    """
    with open(filename, 'rb') as f:
        filename = pickle.load(f)
        return filename
