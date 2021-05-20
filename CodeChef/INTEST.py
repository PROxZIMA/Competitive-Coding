# https://www.codechef.com/viewsolution/43725722

n, k = map(int, input().split())

ans = 0

for i in range(n):
    num = int(input())

    if not num % k:
        ans += 1

print(ans)