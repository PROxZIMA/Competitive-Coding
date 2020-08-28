from math import sqrt

# Naive method: Loop through N and check if every number is prime or not. If prime add to sum. Time complexity is O(√n). Time of execution ~ 8sec for n = 1000000

def prime(n):
    yield 2
    yield 3
    for p in range(5, n+1, 2):
        if p % 3 == 0:
            continue
        else:
            for i in range (5, int(sqrt(p)) + 1, 6):
                if p % i == 0 or p % (i + 2) == 0:
                    break
            else:
                yield p

s = set(prime(1000000))

for _ in range(int(input())):
    n = int(input())
    print(sum(i for i in s if i <= n))


# Sieve implementation: Time complexity of O(n*log(log(n))). Time of execution ~ 2sec for n = 1000000

limit = 1000000
sieve = [0] + [1, 0] * 500000
sieve[0], sieve[1], sieve[2] = 0, 0, 2

p = 3
while p <= limit:
    if sieve[p]:
        sieve[p] = sieve[p-1] + p
        for i in range(p*p, limit+1, p):
            sieve[i] = 0
    else:
        sieve[p] = sieve[p-1]

    sieve[p+1] = sieve[p]
    p += 2


for _ in range(int(input())):
    print(sieve[int(input())])
