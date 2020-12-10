#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumDistances function below.
def minimumDistances(a):
    uniques = {}
    min_distance = len(a)
    for i, e in enumerate(a):
        if e not in uniques:
            uniques[e] = i
            continue

        if min_distance > i - uniques[e]:
            min_distance = i - uniques[e]

    if min_distance == len(a):
        min_distance = -1

    return min_distance

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
