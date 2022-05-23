#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getMinConnectionChange' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY connection as parameter.
#


def getMinConnectionChange(connection):
    assert 1 <= n <= 300000
    assert all(1 <= i <= n for i in connection)

    vis = [0] * (n + 1)
    ct = 0
    col = 0
    for i in range(1, n + 1):
        if not vis[i]:
            cur = i
            col += 1
            while not vis[cur]:
                vis[cur] = col
                cur = connection[cur - 1]
                ct += col == vis[cur]
    ct -= any(i == connection[i - 1] for i in range(1, n + 1))
    return ct


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    connection = list(map(int, input().rstrip().split()))

    result = getMinConnectionChange(connection)

    fptr.write(str(result) + "\n")

    fptr.close()
