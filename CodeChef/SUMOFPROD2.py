# https://www.codechef.com/viewsolution/69783328

MOD = 998244353
L = 100020
factorials = [0] * L
inverse = [0] * L
facInverse = [0] * L

factorials[0] = inverse[0] = inverse[1] = facInverse[0] = facInverse[1] = 1

for i in range(1, L - 8):
    factorials[i] = factorials[i - 1] * i % MOD

for i in range(2, L - 8):
    inverse[i] = MOD - (((MOD // i) * inverse[MOD % i]) % MOD)

for i in range(2, L - 8):
    facInverse[i] = (facInverse[i - 1] * inverse[i]) % MOD


def getProduct(a, b):
    if a < 0 or b > a:
        return 0
    return (((factorials[a] * facInverse[b]) % MOD) * facInverse[a - b]) % MOD


for _ in range(int(input())):
    n = int(input())
    a = input().split()
    one = zero = total = 0
    for num in a:
        if num == "1":
            one += 1
        else:
            zero += 1

    for i in range(one + 1):
        total = (total + i * getProduct(n - i, zero)) % MOD

    print(
        (
            (
                ((total * (zero + 1) - getProduct(n - 2, zero - 1)) % MOD + MOD) % MOD
                + getProduct(n - 2, zero - 1)
            )
            * factorials[one]
            % MOD
        )
        * factorials[zero]
        % MOD
    )
