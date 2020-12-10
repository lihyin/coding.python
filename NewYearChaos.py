#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the minimumBribes function below.
def minimumBribes(q):
    total_count = 0
    for i in range(len(q) - 1, 1, -1):
        #print(i)
        count = 0
        if (q[i] != i + 1):  # swap
            temp = q[i]
            q[i] = q[i - 1]
            q[i - 1] = temp
            count += 1
            print('q:', end='')
            print(q)

            if (q[i - 1] != i):  # further swap
                temp = q[i - 1]
                q[i - 1] = q[i - 2]
                q[i - 2] = temp
                count += 1
                print('q:', end='')
                print(q)

                if (q[i - 2]) != i - 1:
                    print('Too chaotic')
                    return

        total_count += count
        print('count:', end='')
        print(count)
        print('q:', end='')
        print(q)

    print(total_count)
    return


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
