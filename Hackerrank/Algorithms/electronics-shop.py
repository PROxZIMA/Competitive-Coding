from itertools import product

b, n, m = map(int, input().split())
keyboards = map(int, input().split())
drives = map(int, input().split())

chances = list(filter(lambda x: sum(x)<=b, product(keyboards, drives)))
if len(chances)>0:
    print(max(sum(elem) for elem in chances))
else:
    print('-1')
