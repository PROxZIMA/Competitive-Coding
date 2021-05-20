# https://www.codechef.com/viewsolution/37740880

for _ in range(int(input())):
    n, k = map(int, input().split())
    l = list(map(int, input().split()))

    count = 0
    s = 0

    for i in range(n):
        if l[i] > k:
            count = 0
            break

        elif s + l[i] <= k:
            s += l[i]

        else:
            s = l[i]
            count += 1

        if i == n - 1:
            count += 1

    print(-1 if count == 0 else count)