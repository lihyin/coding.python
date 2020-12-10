#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the substrCount function below.
def substrCount(n, s):
    dict = {}
    count = 0
    for i in range(len(s)):
        count += 1
        # if c not in dict:
        #    dict[c] = 1

        if (s[i] == s[i - 1]):
            count += 1
        for j in range(1, i):
            if s[i] == s[i - j]:
                count += 1
            elif s[i] == s[i ]:

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
