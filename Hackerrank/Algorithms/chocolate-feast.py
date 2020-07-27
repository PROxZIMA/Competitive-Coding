# 15 3 2
for _ in range(int(input())):
    n, c, m = map(int, input().split())
    choco = n//c
    w = n//c
    while w >= m:
        choco += w//m
        w = w//m + w%m
        

    print(choco)
