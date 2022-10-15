#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """Get rows in the mat, get values from rows """
    for row in matrix:
        for values in row:
            print("{:d}".format(values), end=" ")
        print()
