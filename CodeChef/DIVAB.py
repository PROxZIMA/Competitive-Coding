# https://www.codechef.com/viewsolution/69672709

def solution(a, b, n):
    if a % b == 0:
        return -1

    if n % a == 0 and n % b != 0:
        return n

    ra = (n + a) % a
    ma = n if (ra == 0) else n + a - ra

    if ma % a == 0 and ma % b != 0:
        return ma

    return ma + a


for _ in range(int(input())):
    a, b, n = list(map(int, input().split()))
    print(solution(a, b, n))
