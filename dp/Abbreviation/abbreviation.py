#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the abbreviation function below.
def abbreviation(a, b):
    dp = [[False for i in range(len(a))] for j in range(len(b))]
    for i in range(len(b)):
        for j in range(len(a)):
            if i == 0 and j == 0:
                dp[i][j] = a[j] == b[i] or a[j].upper() == b[i]
            elif i == 0 and a[j].isupper() and a[j] != b[i]:
                break
            elif i == 0 and (a[j] == b[i] or a[j].upper() == b[i]):
                dp[i][j] = True
            elif i > j:
                dp[i][j] = False
            else:
                if dp[i-1][j-1] and (a[j] == b[i] or a[j].upper() == b[i]):
                    dp[i][j] = True
                elif dp[i][j-1] and a[j].islower():
                    dp[i][j] = True
    print(dp)
    if dp[-1][-1]:
        return "YES"
    return "NO"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        a = input()

        b = input()

        result = abbreviation(a, b)

        fptr.write(result + '\n')

    fptr.close()
