# https://www.codechef.com/viewsolution/44043241

for _ in range(int(input())):
    w1, w2, x1, x2, m = map(int, input().split())
    print(1 if x1 * m <= w2 - w1 <= x2 * m else 0)