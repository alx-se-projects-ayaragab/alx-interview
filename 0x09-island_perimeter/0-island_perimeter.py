#!/usr/bin/python3
"""
island perimeter problem
"""


def island_perimeter(grid):
    """func
    """
    perimeter = 0
    for i, row in enumerate(grid):
        for j, num in enumerate(row):
            if num == 1:
                perimeter += 4
            if i > 0 and grid[i - 1][j] == 1:
                perimeter -= 1
            if j > 0 and grid[i][j - 1] == 1:
                perimeter -= 1
    return perimeter
