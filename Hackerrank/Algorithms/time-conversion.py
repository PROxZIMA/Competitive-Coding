#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(str1):
    if str1[-2:] == "AM" and str1[:2] == "12": 
        return '00' + str1[2:-2] 

    elif str1[-2:] == "AM" or (str1[-2:] == "PM" and str1[:2] == "12"): 
        return str1[:-2]
          
    else:
        return str(int(str1[:2]) + 12) + str1[2:-2] 
if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
