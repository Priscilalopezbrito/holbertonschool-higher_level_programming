#!/usr/bin/python3
"""
This module defines an empty Square class.
"""


class Rectangle:
    """
    Represents a square.
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Defines rectangle size validation.

        Args:
            width (int): The width of rectangle.
            height (int): The height of rectangle
        """
        Rectangle.number_of_instances += 1  # Increment ini count
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
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieves (getter)
        """
        return self.__height

    @height.setter
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
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates the area of a rectangle.

        Returns:
            int: The area of rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates the parameter of a rectangle.

        Returns:
            int: parameter of rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        return '\n'.join('#' * self.__width for r in range(self.__height))

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        if Rectangle.number_of_instances > 0:
            Rectangle.number_of_instances -= 1  # Decrement init count
        print("Bye rectangle...")
