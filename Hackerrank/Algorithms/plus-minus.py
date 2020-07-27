#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    l = len(arr)
    p = sum(1 for i in arr if i>0)
    n = sum(1 for i in arr if i<0)
    z = sum(1 for i in arr if i==0)
    print(f'{p/l:.5f}')
    print(f'{n/l:.5f}')
    print(f'{z/l:.5f}')

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
