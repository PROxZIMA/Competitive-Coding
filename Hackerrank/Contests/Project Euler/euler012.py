from math import ceil, floor, sqrt

def factors(n):
    p, c = 1, 0

    while n % 2 == 0:
        n //= 2
        c += 1
    p *= (c + 1)

    for i in range(3, int(sqrt(n)) + 1, 2):
        c = 0
        while n % i == 0:
            n //= i
            c += 1
        p *= (c + 1)

        if n == 1:
            break

    return p*2 if n > 1 else p


divs = {1 : 1}
dcount = {}

dmax, d, n = 1, 1, 1

while d < 1000:
    n += 1
    t = (n*(n - 1))//2

    # sq = sqrt(t)
    # d=sum(2 for j in range(1, ceil(sq)) if t % j == 0)
    # if ceil(sq) == floor(sq):
    #     d += 1

    d = factors(n)

    divs[n] = d

    if n % 2 == 0: 
        d = divs[n // 2]  * divs[n - 1] 
    else:
        d = divs[(n - 1) // 2]  * d

    if d > dmax :
        for i in range(dmax, d):
            dcount[i] = t
        dmax = d



for _ in range(int(input())):
    print(dcount[int(input())])