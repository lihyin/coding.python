#!/bin/python3

import os
import sys

#
# Complete the countStrings function below.
#
def countStrings(r, l):
    #
    # Write your code here.
    #

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        rl = input().split()

        r = rl[0]

        l = int(rl[1])

        result = countStrings(r, l)

        fptr.write(str(result) + '\n')

    fptr.close()
