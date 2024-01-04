#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing the Pascal's triangle
    Args:
        n (int): number of rows
    Returns:
        list: list of lists of integers
    """
    if n <= 0:
        return []
    pascal = [[1]]
    for i in range(1, n):
        row = [1]
        prev = pascal[i - 1]
        for j in range(len(prev) - 1):
            row.append(prev[j] + prev[j + 1])
        row.append(1)
        pascal.append(row)
    return pascal
