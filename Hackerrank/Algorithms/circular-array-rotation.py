from collections import deque

n, k, q = map(int, input().split())
lst = map(int, input().split())
deq = deque(lst)

for _ in range(k):
    elem = deq.pop()
    deq.appendleft(elem)

for _ in range(q):
    a = int(input())
    print(deq[a])
