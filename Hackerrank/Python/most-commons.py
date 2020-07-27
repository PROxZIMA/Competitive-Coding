from itertools import groupby

def sort(val):
    return val[1]

s = ''.join(sorted(input()))

count = [(i, len(list(j))) for i, j in groupby(s)]

count.sort(key=sort, reverse = True)

for i, j in count[:3]:
    print(i, j)
