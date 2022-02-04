# https://www.codechef.com/viewsolution/63820794

for _ in range(int(input())):
    n, k = map(int, input().split())
    w = list(map(int, input().split()))
    w.sort()

    if k <= n // 2:
        print(abs(sum(w[:k]) - sum(w[k:])))
    else:
        print(abs(sum(w[:n - k]) - sum(w[n - k:])))
