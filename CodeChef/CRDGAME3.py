# https://www.codechef.com/viewsolution/36402569

from math import ceil
for _ in range(int(input())):
    pc, pr = map(int, input().split())
    c, r = ceil(pc / 9), ceil(pr / 9)
    if c < r:
        print(0, c)
    else:
        print(1, r)