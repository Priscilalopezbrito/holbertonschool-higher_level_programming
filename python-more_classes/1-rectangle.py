#!/usr/bin/python3
"""
This module defines an empty Square class.
"""


class Rectangle:
    """
    Represents a square.
    """
    def __init__(self, width=0, height=0):
        """
        Defines rectangle size validation.

        Args:
            width (int): The width of rectangle.
            height (int): The height of rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Retrieves (getter)
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets rect w

        Args:
            value (int): Value of height
            integers representing the position.

        Raises:
            TypeError: height must be an integer.
            ValueError: If height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieves (getter)
        """
        return self.__height

    @width.setter
    def height(self, value):
        """
        Sets rect h

        Args:
            value (int): Value of width
            integers representing the position.

        Raises:
            TypeError: width must be an integer.
            ValueError: If height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value
