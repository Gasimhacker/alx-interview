#!/usr/bin/python3
"""
Pascal's triangle implementation
"""


def pascal_triangle(n):
    """
    Return pascal's triangle of n rows
    """
    if (n <= 0):
        return []
    triangle = [[1]]
    for i in range(1, n):
        new_row = triangle[i - 1] + [1]
        for j in range(1, i):
            new_row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(new_row)
    return triangle
