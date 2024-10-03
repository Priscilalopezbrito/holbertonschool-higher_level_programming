#!/usr/bin/python3
"""
Pascal's Triangle
"""


def pascal_triangle(n):
    """
    Pascal's Triangle
    """
    pasc = []
    if n <= 0:
        return pasc
    pasc = [[1]]  # Always starts with 1
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(pasc[i - 1][j - 1] + pasc[i - 1][j])
        row.append(1)
        pasc.append(row)

    return pasc
