#!/usr/bin/python3
"""
Class BaseGeometry
Class Rectangle
"""


Rectangle = __import__('9-rectangle').Rectangle
"""superclass import """


class Square(Rectangle):
    """
    Class Square
    """

    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        return (self.__size)**2

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
