#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square = []
    for row in matrix:
        squared = [i**2 for i in row]
        square.append(squared)
    return square
