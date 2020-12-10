#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    dict = {} #key: substr, value: count

    for substr_len in range(1, len(s)):
        dict[substr_len] = {}
        for i in range(0, len(s) - substr_len + 1):
            sorted_substr = ''.join(sorted(s[i:i + substr_len]))
            if sorted_substr not in dict[substr_len]:
                dict[substr_len][sorted_substr] = 0

            for j in range(i + 1, len(s) - substr_len + 1):
                sorted_substr1 = ''.join(sorted(s[j:j+substr_len]))
                if sorted_substr == sorted_substr1:
                    dict[substr_len][sorted_substr] += 1

    total = 0
    for e,v in dict.items():
        for e1,v1 in v.items():
            total += v1

    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
