# https://www.codechef.com/viewsolution/36087808

for _ in range(int(input())):
    n = int(input())
    x, y = 0, 0

    for _ in range(4*n-1):
        x1, y1 = map(int, input().split())
        x ^= x1 
        y ^= y1

    print(x, y)