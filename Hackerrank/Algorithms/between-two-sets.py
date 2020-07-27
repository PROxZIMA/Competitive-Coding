#!/bin/python3

import math
import os
import random
import re
import sys

def getTotalX(a, b):
    count = 0
    for i in range(a[0], b[0]+1, 1):
        c1 = sum(1 for j in a if i%j ==0)
        c2 = sum(1 for j in b if j%i ==0)
        if c1==len(a) and c2 == len(b):
            count+=1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n, m = map(int, input().rstrip().split())

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
