#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the maxMin function below.
def maxMin(k, arr):
    arr = sorted(arr)
    res = arr[-1]

    for ind in range(len(arr) - k + 1):
        res = min(res, arr[ind + k - 1] - arr[ind])
        # print("ind = {} arr = {} res = {}".format(ind, arr[ind:ind+k], res))

    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    k = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()