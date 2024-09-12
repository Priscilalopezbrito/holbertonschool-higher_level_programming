#!/usr/bin/python3
"""
Module contains function that adds two integers.
"""


def add_integer(a, b=98):
    """
    Calculate sum of a two integers/floats a and b.

    Parameters:
        a (int, float): First number in sum
        b (int, float): Second number in sum

    Returns:
        int: Sum of the two numbers
    Raises:
        TypeError: If 'a' or 'b' are not integers or floats
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
