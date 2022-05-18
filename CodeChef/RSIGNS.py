# https://www.codechef.com/viewsolution/72739139

MOD = 1000000007

def powmod(n, m):
    pow2 = 2
    result = 1
    while n > 0:
        if n % 2 == 1:
            result = (result * pow2) % m
        pow2 = (pow2 * pow2) % m
        n >>= 1
    return result

for _ in range(int(input())):
    k = int(input())
    sol = powmod(k-1, MOD)
    print((sol * 10) % MOD)
