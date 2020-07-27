#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    l = []
    
    for elem in grades:
        rem = elem%5
        if rem==0:
            l.append(elem)
        elif (rem>2 and elem > 37):
            l.append(elem + (5 - rem))
        else:
            l.append(elem)
    return l
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = [int(input().strip()) for _ in range(grades_count)]

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
