# https://www.codechef.com/viewsolution/63835655

import numpy as np

for _ in range(int(input())):
    n = int(input())
    m = int(input())
    time = np.zeros(m, dtype=int)

    for i in range(n):
        l, r = map(int, input().split())
        time[l - 1 : r] += 1

    print(max(time))
