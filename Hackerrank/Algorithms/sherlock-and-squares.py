from math import floor, ceil, sqrt

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(floor(sqrt(b))-ceil(sqrt(a))+1)
