# https://www.codechef.com/viewsolution/63817260

for _ in range(int(input())):
    n = int(input())
    s = list(map(int, input().split()))
    s.sort()

    ans = float('INF')

    for i in range(1, n):
        ans = min(ans, abs(s[i] - s[i - 1]))

    print(ans)
