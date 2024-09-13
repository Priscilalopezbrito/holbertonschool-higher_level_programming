#!/usr/bin/python3
"""
Module contains function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides elements of matrix by a number.
    Args:
        matrix (list of lists): The matrix to be divided.
        div (int or float): The number to divide by.
    Returns:
        list: A new matrix with all elements divided by div.
    Raises:
        TypeError: non-numbers, div not number, rows aren't same size.
        ZeroDivisionError: If div is 0.
    """
