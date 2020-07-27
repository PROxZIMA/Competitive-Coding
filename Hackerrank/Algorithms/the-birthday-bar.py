#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(n, s, d, m):
    count = 0
    for i in range(n-m+1):
        if sum(s[i:i+m]) == d:
            count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    d, m = map(int, input().rstrip().split())

    result = birthday(n, s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
