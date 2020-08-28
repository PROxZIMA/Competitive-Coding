from functools import reduce

def mul(a, b):
    return a * b

for _ in range(int(input())):
    n, k = map(int, input().split())
    num = input()
    maxi = 0
    for i in range(n-k+1):
        m = reduce(mul, map(int, list(num[i : i+k])))
        if maxi < m:
            maxi = m
    print(maxi)