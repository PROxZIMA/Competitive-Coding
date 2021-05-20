# https://www.codechef.com/viewsolution/44674409

from itertools import accumulate

def binSearch(arr: tuple, r: int, lens: int, k: int, siz: int) -> int:
    s, l, siz2, total = 1, lens, siz ** 2, lens + 1

    while (s <= l):
        m = int((s + l) / 2)
        avg = (arr[r][m] - arr[r][m - siz] - arr[r - siz][m] + arr[r - siz][m - siz]) / siz2
        if (avg >= k):
            total = m
            l = m - 1
        else:
            s = m + 1
    return (lens - total + 1)


def update(inp: list) -> tuple:
    global a
    a = tuple(x + y for x, y in zip(a, accumulate(map(int, inp), lambda x, y : x + y)))
    return a

for _ in range(int(input())):
    n, m, k = map(int, input().split())
    a = (0,) * (m + 1)
    arr = (a,) + tuple(update([0] + input().split()) for _ in range(n))

    ans = 0
    for leng in range(1, min(n, m) + 1):
        for row in range(leng, n + 1):
            ans += binSearch(arr, row, m, k, leng)
    print(ans)