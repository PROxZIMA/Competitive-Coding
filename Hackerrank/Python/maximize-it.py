from itertools import product

k, m = map(int, input().split())
L = [list(map(int, input().split()))[1: ] for _ in range(k)]

print(max(sum(i**2 for i in elem)%m for elem in product(*L)))
