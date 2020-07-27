from collections import deque

d = deque()

for _ in range(int(input())):
    op, *num = input().split()
    getattr(d, op)(*map(int, num))

print(' '.join(map(str, d)))
