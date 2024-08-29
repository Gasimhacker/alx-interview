#!/usr/bin/python3
"""Calculate the perimeter of an island"""


def island_perimeter(grid):
    """Find the perimeter of the island described in grid"""
    perimeter = 0
    n1 = len(grid)
    n2 = len(grid[0]) if n1 > 0 else 0
    for i in range(n1):
        for j in range(n2):
            if (grid[i][j] == 0):
                continue
            cell_len = 4
            if (i and grid[i - 1][j]):
                cell_len -= 1
            if ((i + 1 < n1) and grid[i + 1][j]):
                cell_len -= 1
            if (j and grid[i][j - 1]):
                cell_len -= 1
            if ((j + 1 < n2) and grid[i][j + 1]):
                cell_len -= 1
            perimeter += cell_len
    return perimeter
