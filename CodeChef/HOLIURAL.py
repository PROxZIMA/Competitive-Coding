# https://www.codechef.com/viewsolution/64266779

for _ in range(int(input())):
    n, k = map(int, input().split())
    d = map(int, input().split())
    r = map(int, input().split())
    ans = float('inf')

    for i, j in zip(d, r):
        ans = min(ans, i * k + j)

    print(ans)
