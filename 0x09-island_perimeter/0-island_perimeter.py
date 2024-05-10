#!/usr/bin/python3
"""
Calculate the perimeter of a island
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of a 2 matrix
    """
    perimeter = 0
    if grid is None:
        return 0

    if type(grid) != list:
        return 0

    for i in range(len(grid)):
        for e in range(len(grid[i])):
            if grid[i][e] == 1:
                if i == 0 or grid[i - 1][e] == 0:
                    perimeter += 1
                if i == len(grid) - 1 or grid[i + 1][e] == 0:
                    perimeter += 1
                if e == 0 or grid[i][e - 1] == 0:
                    perimeter += 1
                if e == len(grid[i]) - 1 or grid[i][e + 1] == 0:
                    perimeter += 1

    return perimeter