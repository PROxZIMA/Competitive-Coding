from functools import reduce

def gcd(x, y):
    x, y = max(x, y), min(x, y)
    while True:
        r = x % y
        x, y = y, r
        if r == 0:
            g = x
            break
    return g

def lcm(a, b):
    return a*b//gcd(a, b)

for _ in range(int(input())):
    n = int(input())
    print(reduce(lcm, range(1, n + 1)))
