# https://www.codechef.com/viewsolution/43419253

from math import log

for _ in range(int(input())):
    c = int(input())
    twod = 2 ** (int(log(c, 2)) + 1)
    n1 = twod // 2 - 1
    n2 = c ^ n1
    print(n2 * n1)