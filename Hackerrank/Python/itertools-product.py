from itertools import product
print(' '.join(map(str, product(map(int, input().split()), map(int, input().split())))))
