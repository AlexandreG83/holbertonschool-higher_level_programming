#!/usr/bin/python3
"""
Module that provides a function to divide all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div.

    Args:
        matrix (list of lists of int/float): matrix to divide
        div (int/float): number to divide by

    Returns:
        list: new matrix with elements divided by div, rounded to 2 decimals

    Raises:
        TypeError: if matrix elements are not numbers or rows not same size
        TypeError: if div is not a number
        ZeroDivisionError: if div == 0
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if (not isinstance(matrix, list) or
            any(not isinstance(row, list) for row in matrix)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    row_length = len(matrix[0]) if matrix else 0
    new_matrix = []
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
        new_row = []
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists)"
                    "of integers/floats")
            new_row.append(round(item / div, 2))
        new_matrix.append(new_row)
    return new_matrix
