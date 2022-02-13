# https://www.codechef.com/viewsolution/63825725

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    freq = [0] * 1001
    for i in a:
        freq[i] += 1

    area, flag = 1, False

    for i in range(1000, -1, -1):
        if not flag and freq[i] >= 2:
            area *= i
            flag = not flag
            freq[i] -= 2
        if flag and freq[i] >= 2:
            area *= i
            flag = not flag
            break

    print(-1 if flag else area)
