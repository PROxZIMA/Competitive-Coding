from itertools import combinations

n, d = map(int, input().split())
lst = list(map(int, input().split()))

count = 0
for elem in lst:
    if elem + d in lst and elem + 2*d in lst:
        count += 1

print(count)
