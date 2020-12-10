#!/bin/python3

import math
import os
import random
import re
import sys


'''
# this approach will timeout
def digit_sum(n):
    total = 0
    while n > 0:
        total += n - (n // 10) * 10
        n = n // 10
    return total

def super_digit(n):
    if n < 10:
        return n

    total = digit_sum(n)
    return super_digit(total)

# Complete the superDigit function below.
def superDigit(n, k):
    n = int(n)
    d = 0
    for i in range(k):
        d += n * (10 ** (i * k))

    return super_digit(d)
'''

# Complete the superDigit function below.
def helper(n_s):
    sum_str = 0
    for char in n_s:
        sum_str += int(char)
    if sum_str < 10:
        return sum_str
    return helper(str(sum_str))


def superDigit(n, k):
    s = 0
    for char in n:
        s += int(char)
    n = s * k
    return helper(str(n))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
