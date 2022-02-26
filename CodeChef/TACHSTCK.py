n, d = map(int, input().split())
c = sorted(int(input()) for _ in range(n))
i = ans = 0

while i < n - 1:
    if c[i + 1] - c[i] <= d:
        i += 2
        ans += 1
    else:
        i += 1

print(ans)
