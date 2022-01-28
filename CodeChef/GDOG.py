# https://www.codechef.com/viewsolution/63762291

for _ in range(int(input())):
    n, k = map(int, input().split())
    ans = -float('INF')

    for i in range(1, k + 1):
        ans = max(ans, n % i)

    print(ans)
