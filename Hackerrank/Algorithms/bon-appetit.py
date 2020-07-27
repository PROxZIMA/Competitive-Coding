#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    bill.pop(k)
    bactual = sum(bill)//2
    if b>bactual:
        print(b-bactual)
    else:
        print('Bon Appetit')
if __name__ == '__main__':
    n, k = map(int, input().split())

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
