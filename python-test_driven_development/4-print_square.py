#!/usr/bin/python3
"""
Module contains function that prints a square with the character #.
"""


def print_square(size):
    """
    Prints a square with '#'.

    Args:
        size (int): The size of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for p in range(size):
        print("#" * size)
