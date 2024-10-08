#!/usr/bin/python3
"""
Class BaseGeometry
Class Rectangle
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

    def area(self):  # Override BaseGeometry method
        return (self.__width * self.__height)

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
