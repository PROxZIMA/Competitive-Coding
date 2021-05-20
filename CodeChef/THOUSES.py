# https://www.codechef.com/viewsolution/46554769

from collections import defaultdict
import sys
sys.setrecursionlimit(300000)

def solution(k: str, l: str):
    for c in graph[k]:
        if c == l:
            continue
        solution(c, k)

    arr = sorted((value[c], c) for c in graph[k] if c != l)

    for key, val in zip(arr, range(len(arr), 0, -1)):
        value[k] += val * key[0]


for _ in range(int(input())):
    graph = defaultdict(list)
    value = defaultdict(lambda: 1)
    n, x = map(int, input().split())

    for i in range(n-1):
        p, c = input().split()
        graph[p].append(c)
        graph[c].append(p)

    solution('1', '0')

    print((value['1'] * x) % 1000000007)