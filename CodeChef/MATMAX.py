# https://www.codechef.com/viewsolution/63832507

for _ in range(int(input())):
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for i in range(n)]
    ans = -float('INF')

    for row in a:
        mini, maxi = float('INF'), -float('INF')
        for num in row:
            mini = min(mini, num)
            maxi = max(maxi, num)
        ans = max(ans, abs(mini - maxi))

    print(ans)
