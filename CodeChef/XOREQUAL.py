# https://www.codechef.com/viewsolution/46099198

MOD = 1000000007

for _ in range(int(input())):
    n = int(input()) - 1

    ans = 1
    b = 2
    while 0 < n:
        if n % 2:
            ans = (ans * b) % (MOD)
        n = n // 2
        b = (b * b) % MOD
    print(ans)

    # print((2 ** (n - 1)) % (MOD))
