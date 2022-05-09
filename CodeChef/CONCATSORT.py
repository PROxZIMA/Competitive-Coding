# https://www.codechef.com/viewsolution/69682931


def solution(n, a, sa):
    flag = 0
    i = j = 0
    while j < n:
        while i < n and j < n:
            if flag == 2:
                return "NO"
            if a[i] == sa[j]:
                j += 1
            i += 1
            if i == n:
                flag += 1
                i = 0
    return "YES"


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    sa = sorted(a)
    print(solution(n, a, sa))
