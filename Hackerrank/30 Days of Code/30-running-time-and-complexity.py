from math import sqrt

def prime(p):
    if p <= 1:
        return False

    elif p <= 3:
        return True

    elif p % 2 == 0 or p % 3 == 0:
        return False

    else:
        for i in range (5, int(sqrt(p)) + 1, 6):
            if p % i == 0 or p % (i + 2) == 0:
                return False
        else:
            return True


for _ in range(int(input())):
    n = int(input())
    if prime(n):
        print('Prime')
    else:
        print('Not prime')
