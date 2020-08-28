for _ in range(int(input())):
    n, k = map(int, input().split())
    l = list(map(int, input().split()))

    count = 0
    s = 0
    l.append(1001)

    for i in range(n):
        if s + l[i] + l[i + 1] <= k:
            s += l[i]
            if i != n - 1:
                continue

        count += 1
        s = 0
    if len(l) == 2 and l[0] > k:
        count = 0
    print(-1 if count == 0 else count)