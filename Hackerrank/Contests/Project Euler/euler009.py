for _ in range(int(input())):
    n = int(input())
    maxi = -1
    for a in range(1, int(n /3 ) + 1):
        b = (n * n - 2 * n * a) // (2 * n - 2 * a)
        c = n - a - b
        p = a * b * c
        if a * a + b * b == c * c and maxi < p:
            maxi = p
    print(maxi)