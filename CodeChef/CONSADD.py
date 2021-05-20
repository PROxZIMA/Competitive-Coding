# https://www.codechef.com/viewsolution/43556793

import numpy as np

for _ in range(int(input())):
    row, col, x = map(int, input().split())
    a = np.array([input().split() for _ in range(row)], int)
    b = np.array([input().split() for _ in range(row)], int)

    diff = a - b

    for r in range(row):
        for c in range(col - x + 1):
            diff[r, c : c + x] -= diff[r, c]

    for r in range(row - x + 1):
        for c in range(col - x + 1, col):
            diff[r : r + x, c] -= diff[r, c]

    print('Yes' if np.all(diff == 0) else 'No')

