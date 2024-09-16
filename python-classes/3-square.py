!/usr/bin/python3
"""
This module defines Area of a square.
"""


class Square:
    """
    Represents a square.
    """
    def __init__(self, size=0):
        """
        Defines square size validation.

        Args:
            size (int): The size of the square.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculates square area.

        Returns:
            int: The area of the square.
        """

        return self.__size ** 2
