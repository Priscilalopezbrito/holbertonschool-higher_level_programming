#!/usr/bin/ env python3
import pickle
"""
Serialize and deserialize custom Python
objects using the pickle module.
"""


class CustomObject:
    """
    Class named CustomObject
    """
    def __init__(self, name, age, is_student):
        """
        init
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Print out the object’s attributes.
        """
        print('Name: {}'.format(self.name))
        print('Age: {}'.format(self.age))
        print('Is Student: {}'.format(self.is_student))

    def serialize(self, filename):
        """
        Serialize the current instance of the object
        and save it to the provided filename.
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)

        except (pickle.PicklingError, IOError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Using the pickle module, it will load and
        return an instance of the CustomObject
        from the provided filename.
        """
        try:
            with open(filename, 'rb') as f:
                obj = pickle.load(f)
                return obj
        except (pickle.UnpicklingError, IOError, FileNotFoundError):
            return None
