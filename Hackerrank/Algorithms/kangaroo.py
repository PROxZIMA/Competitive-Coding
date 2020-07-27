#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    i = 0
    if (x2>x1 and v2>v1) or v1 == v2:
        return 'NO'
    elif ((x2-x1)%(v1-v2) == 0):
        return 'YES'
    else:
        return 'NO'
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1, v1, x2, v2 = map(int, input().split())

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
