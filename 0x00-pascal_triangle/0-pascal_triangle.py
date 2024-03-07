#!/usr/bin/python3
"""
Pascal's Triangle
"""
from math import factorial


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing 
    the Pascal’s triangle of n
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
