#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superReducedString function below.
def superReducedString(input):
    s = []

    for c in input:
        if not s:
            s.append(c)
        else:
            if s[-1] == c:
                s.pop()
            else:
                s.append(c)

    if not s:
        return "Empty String"
    else:
        return ''.join(s)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
