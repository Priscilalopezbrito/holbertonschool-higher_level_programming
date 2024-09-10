#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        if len(row) > 0:
            print(" ".join("{:d}".format(n) for n in row))
        else:
            print("")
