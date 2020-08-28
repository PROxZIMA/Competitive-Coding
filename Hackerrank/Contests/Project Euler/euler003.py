import math

for _ in range(int(input())):
    n = int(input())
    p_max = 0

    while n % 2 == 0:
        n //= 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            n //= i
            p_max = i

        if n == 1:
            break

    print(n if n > 2 else p_max)
