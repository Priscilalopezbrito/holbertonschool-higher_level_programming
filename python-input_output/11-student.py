#!/usr/bin/python3
"""
Student to JSON
"""


class Student:
    """
    Class Student that defines a student
    """
    def __init__(self, first_name, last_name, age):
        """
        Instantiation with first_name, last_name and age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation
        of a Student instance
        """
        if attrs is None:
            return self.__dict__
        return {a: getattr(self, a) for a in attrs if hasattr(self, a)}

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance
        """
        for key, value in json.items():
            setattr(self, key, value)
