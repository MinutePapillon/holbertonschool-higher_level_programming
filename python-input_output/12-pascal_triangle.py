#!/usr/bin/python3
"""
Function that returns Pascal's triangle of n.
"""


def pascal_triangle(n):
    """
    Return a list of lists of integers representing Pascal’s triangle of n.

    Args:
        n (int): Number of rows.

    Returns:
        list: Pascal's triangle represented as a list of lists.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        prev = triangle[i - 1]
        for j in range(1, i):
            row.append(prev[j - 1] + prev[j])
        row.append(1)
        triangle.append(row)

    return triangle
