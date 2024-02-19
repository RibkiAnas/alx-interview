#!/usr/bin/python3
"""
Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
    Given an n x n 2D matrix, rotate it
    """
    n = len(matrix)
    for i in range(n // 2):
        offset = 0
        for j in range(i, n - i - 1):
            top = matrix[i][j]
            matrix[i][j] = matrix[n - offset - 1][i]
            matrix[n - offset - 1][i] = matrix[n - i - 1][n - offset - 1]
            matrix[n - i - 1][n - offset - 1] = matrix[j][n - i - 1]
            matrix[j][n - i - 1] = top
            offset += 1
    return matrix
