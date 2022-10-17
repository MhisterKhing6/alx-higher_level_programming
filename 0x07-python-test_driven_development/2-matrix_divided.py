#!/usr/bin/python3
def matrix_divided(matrix, div):
    compyMatrix = []
    """Check if div is a number"""
    if type(div) not in [float, int]:
        raise TypeError("div must be a number")
    """Check if div is zero"""
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        """Check if they have the same size"""
        for second_rows in matrix:
            if len(row) != len(second_rows):
                raise TypeError("Each row of the matrix must"
                                " have the same size")
        """For rows of the matrix"""
        copyrow = []
        for i in range(len(row)):
            """Check if matrix is of integer or float """
            if type(row[i]) not in [float, int]:
                raise TypeError("matrix must be a matrix "
                                "(list of lists) of integers/floats")
            else:
                copyrow.append(round(row[i]/div,2))
        compyMatrix.append(copyrow)
    return compyMatrix

