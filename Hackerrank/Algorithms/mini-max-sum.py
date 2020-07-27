#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    l = []
    for i in range(len(arr)):
        c = arr[:]
        c.pop(i)
        l.append(sum(c))
    print(f'{min(l)} {max(l)}')

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
