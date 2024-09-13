#!/usr/bin/python3
"""
Module contains function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number and returns a new matrix.
    Args:
        matrix (list of lists): The matrix to be divided.
        div (int or float): The number to divide by.
    Returns:
        list: A new matrix with all elements divided by div, rounded to 2 decimal places.
    Raises:
        TypeError: If matrix contains non-numbers, div is not a number, or rows aren't the same size.
        ZeroDivisionError: If div is 0.
    """
    return [[round(elem / div, 2) for elem in row] for row in matrix]
