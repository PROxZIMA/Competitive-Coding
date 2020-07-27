from collections import defaultdict
d = defaultdict(list)

n, m = map(int, input().split())

for i in range(n):
    a = input()
    d[a].append(str(i+1))

for _ in range(m):
    b = input()
    if b not in d.keys():
        print('-1')
    else:
        print(' '.join(d[b]))
