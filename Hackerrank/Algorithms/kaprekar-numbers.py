p, q = int(input()), int(input())
lst = []
for i in range(p, q+1):
    sq = str(i*i)
    l = len(str(i))
    try:
        x, y = int(sq[:-l]), sq[-l:]
    except ValueError:
        x, y = 0, sq[-l:]
    if x + int(y) == i:
        lst.append(str(i))

if lst == []:
    print('INVALID RANGE')
else:
    print(' '.join(lst))
