from itertools import count, groupby

s = input()

for i, j in groupby(s):
    print(f'({len(list(j))}, {i})', end = ' ')
