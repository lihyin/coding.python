#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the surfaceArea function below.
def surfaceArea(A):
    total = 0
    for i in range(len(A)):
        for j in range(len(A[i])):
            total += A[i][j] * 6 - (A[i][j] - 1) * 2
            if (i != 0):
                if (A[i-1][j] < A[i][j]):
                    total -= A[i-1][j]
                else:
                    total -= A[i][j]

            if (j != 0):
                if (A[i][j-1] < A[i][j]):
                    total -= A[i][j-1]
                else:
                    total -= A[i][j]

            if (i != len(A)-1):
                if (A[i+1][j] < A[i][j]):
                    total -= A[i+1][j]
                else:
                    total -= A[i][j]

            if (j != len(A[i])-1):
                if (A[i][j+1] < A[i][j]):
                    total -= A[i][j+1]
                else:
                    total -= A[i][j]

    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    HW = input().split()

    H = int(HW[0])

    W = int(HW[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    fptr.write(str(result) + '\n')

    fptr.close()
