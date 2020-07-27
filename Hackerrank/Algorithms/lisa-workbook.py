from math import ceil
from itertools import count, islice

n, k = map(int, input().split())
arr = map(int, input().split())

total = 0
c = 1
for elem in arr:
    l = iter(range(1, elem+1))
    for i, j in zip(count(c), iter(lambda: tuple(islice(l, k)), ())):
        if i in j:
            total += 1
        c += 1

print(total)
