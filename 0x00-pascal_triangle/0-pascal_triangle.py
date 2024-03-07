#!/usr/bin/python3
"""
Pascal's Triangle
"""
from math import factorial


def pascal_triangle(n):
    """
        Returns the Pascal's triangle of n
        Args:
            n (int): number of rows
    """
    if n <= 0:
        return []
    triangle = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            row.append(factorial(i) // (factorial(j) * factorial(i - j)))
        triangle.append(row)
    return triangle
