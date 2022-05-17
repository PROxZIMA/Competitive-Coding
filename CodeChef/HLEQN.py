# https://www.codechef.com/viewsolution/71193589

from math import sqrt


def divisor(n):
    s = sqrt(n)

    # Perfect square
    if n == int(s + 0.5) ** 2:
        return "YES"

    i = 3
    while i <= s:
        if n % i == 0:
            return "YES"
        i += 1
    return "No"


for _ in range(int(input())):
    a = int(input())
    # 2x + 2y + xy = a
    # (x + 2)(y + 2) = 4 + a
    print(divisor(4 + a))
