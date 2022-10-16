#!/usr/bin/python3
"""Square the matrix"""


def square_matrix_simple(matrix=[]):
    matrix2 = []
    for row in matrix:
        temp = []
        for value in row:
            temp.append(value**2)
        matrix2.append(temp)
    return matrix2
