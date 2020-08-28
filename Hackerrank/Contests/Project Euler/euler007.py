from math import sqrt

def prime():
    yield 2
    yield 3
    for p in range(5, 104730, 2):
        if p % 3==0:
            continue
        else:
            for i in range (5, int(sqrt(p)) + 1, 6):
                if p % i == 0 or p % (i + 2) == 0:
                    break
            else:
                yield p

l = list(prime())

for _ in range(int(input())):
    n = int(input())
    print(l[n-1])