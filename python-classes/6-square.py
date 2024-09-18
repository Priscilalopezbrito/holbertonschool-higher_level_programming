#!/usr/bin/python3
"""
This module prints a square.
"""


class Square:
    """
    Represents a square.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Defines square size validation.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
        self.__posotion = position

    @property
    def size(self):
        """
        Retrieves (getter)
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets size of square with validation.

        Args:
            value (int): Size of square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints in stdout the square with the character #
        """
        if self.size == 0:
            print("")
        else:
            for p in range(self.size):
                print("#" * self.size)

    @property
    def position(self):
        """
        Retrieves (getter)
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Coordinates of a square

        Args:
            value (int): Size of square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) < 2:
            raise TypeError("position must be a tuple of 2 positive integers")
