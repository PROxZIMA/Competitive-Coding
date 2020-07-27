#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    mini = scores[0]
    mini_c = 0
    maxi = scores[0]
    maxi_c = 0
    for i in scores:
        if i>maxi:
            maxi = i
            maxi_c+=1
        elif i<mini:
            mini = i
            mini_c+=1
    return [maxi_c, mini_c]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
