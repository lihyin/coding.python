#!/bin/python3

import math
import os
import random
import re
import sys

def find_adjacent(grid, i, j):
    count = 0
    if i < 0 or j < 0 or i >= n or j >= m:
        return 0
    if grid[i][j] == 0:
        return 0

    count += 1
    grid[i][j] -= 1

    count += find_adjacent(grid, i-1, j-1)
    count += find_adjacent(grid, i-1, j)
    count += find_adjacent(grid, i-1, j+1)
    count += find_adjacent(grid, i+1, j-1)
    count += find_adjacent(grid, i+1, j)
    count += find_adjacent(grid, i+1, j+1)
    count += find_adjacent(grid, i, j-1)
    count += find_adjacent(grid, i, j+1)

    return count

# Complete the maxRegion function below.
def maxRegion(grid):
    biggest = 0
    for i in range(n):
        for j in range(m):
            result = find_adjacent(grid, i, j)
            if result > biggest:
                biggest = result

    return biggest

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    m = int(input())

    grid = []

    for _ in range(n):
        grid.append(list(map(int, input().rstrip().split())))

    res = maxRegion(grid)

    fptr.write(str(res) + '\n')

    fptr.close()
