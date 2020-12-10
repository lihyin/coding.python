#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    e = expenditure[0:d]
    e.sort()
    expenditure[0:d] = e

    if d % 2 == 0:
        median = (expenditure[d // 2] + expenditure[d // 2 - 1]) / 2
    else:
        median = expenditure[d // 2]

    count = 0

    for i in range(d, len(expenditure) - 1):
        if expenditure[i] >= median * 2:
            count += 1

        # insert next to the previous sorted expenditure
        for j in range(i - d, i):
            if expenditure[j] > expenditure[i + 1]:
                # insert
                temp = expenditure[i]
                expenditure[j+1:i] = expenditure[j:i-1]
                expenditure[j] = temp

        if d % 2 == 0:
            median = (expenditure[i - d / 2] + expenditure[i - d / 2 - 1]) / 2
        else:
            median = expenditure[i - d // 2]

    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
