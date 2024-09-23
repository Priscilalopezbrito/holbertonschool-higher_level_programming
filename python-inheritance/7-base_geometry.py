#!/usr/bin/python3
"""
Class BaseGeometry
Improve Geometry
"""


class BaseGeometry:
    """
    BaseGeometry class
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        that validates value
        """
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
