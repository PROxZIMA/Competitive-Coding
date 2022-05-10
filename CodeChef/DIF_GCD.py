# https://www.codechef.com/viewsolution/69680416

for _ in range(int(input())):
    n, m = list(map(int, input().split()))
    sol = -1
    x, y = n, m
    i = 1
    while m // i >= n:
        a = m // i
        b = a * i
        if b - a > sol:
            sol = b - a
            x, y = a, b
        i += 1
    print(x, y)
