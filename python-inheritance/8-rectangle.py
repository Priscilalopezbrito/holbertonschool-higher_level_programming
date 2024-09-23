#!/usr/bin/python3
"""
Class BaseGeometry
Improve Geometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""superclass import """

class Rectangle(BaseGeometry):
    """
    Class Rectangle inherits from BaseGeometry
    """
    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
