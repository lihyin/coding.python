#!/bin/python3

import math
import os
import random
import re
import sys
# import numpy

'''
# using x, y line equation doesn't work
# Complete the matrixRotation function below.
def matrixRotation(matrix, r):
    # initial matrixR
    matrixR = []
    for i in range(len(matrix)):
        columns = []
        for j in range(len(matrix[0])):
            columns.append(0)
        matrixR.append(columns)

    m = len(matrix) - 1
    n = len(matrix[0]) - 1

    for c in range(r):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if (i <= m / n * j) and ((n - i) <= n / m * j) and ((i + 1) < len(matrix[i])):
                    matrixR[i + 1][j] = matrix[i][j]
                if (i <= m / n * j) and ((n - i) >= n / m * j) and ((j - 1) > 0):
                    matrixR[i][j - 1] = matrix[i][j]
                if (i >= m / n * j) and ((n - i) >= n / m * j) and ((i - 1) > 0):
                    matrixR[i - 1][j] = matrix[i][j]
                if (i >= m / n * j) and ((n - i) <= n / m * j) and ((j + 1) < len(matrix[i])):
                    matrixR[i][j + 1] = matrix[i][j]

    print(matrixR)
'''

'''
# Have a duplicated matrix
# Complete the matrixRotation function below.
def matrixRotation(matrix, r):
    n = len(matrix)
    m = len(matrix[0])

    # initial matrixR
    matrixR = []
    for i in range(n):
        columns = []
        for j in range(m):
            columns.append(0)
        matrixR.append(columns)

    for _ in range(r):
        c = 0
        while (c < n / 2) and (c < m / 2):
            for j in range(1 + c, m - c):
                matrixR[c][j - 1] = matrix[c][j]
                matrixR[n - c - 1][j] = matrix[n - c - 1][j - 1]
            for i in range(1 + c, n - c):
                matrixR[i][c] = matrix[i - 1][c]
                matrixR[i - 1][m - c - 1] = matrix[i][m - c - 1]
            c += 1

        # copy matrixR to matrix
        for i in range(n):
            for j in range(m):
                matrix[i][j] = matrixR[i][j]

    for n1 in range(n):
        for m1 in range(m):
            print(matrixR[n1][m1], end=' ')
        print('')

    return
'''

# Without duplicated matrix
# Complete the matrixRotation function below.
def matrixRotation(matrix, r):
    n = len(matrix)
    m = len(matrix[0])

    for _ in range(r):
        c = 0
        while (c < n / 2) and (c < m / 2):
            lt = matrix[c][c]
            rb = matrix[n - c - 1][m - c - 1]

            for j in range(1 + c, m - c):
                matrix[c][j - 1] = matrix[c][j]
                matrix[n - c - 1][m - j] = matrix[n - c - 1][m - j - 1]
            for i in range(1 + c, n - c):
                matrix[n - i][c] = matrix[n - i - 1][c]
                matrix[i - 1][m - c - 1] = matrix[i][m - c - 1]

            matrix[c + 1][c] = lt
            matrix[n - 2 - c][m - 1 - c] = rb

            c += 1

    for n1 in range(n):
        for m1 in range(m):
            print(matrix[n1][m1], end=' ')
        print('')

    return

if __name__ == '__main__':
    mnr = input().rstrip().split()

    m = int(mnr[0])

    n = int(mnr[1])

    r = int(mnr[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r)
