# https://www.codechef.com/viewsolution/46310372

for _ in range(int(input())):
    n, m = map(int, input().split())
    arr = [1] * (n + 1)
    ans = 0
    for b in range(2, n + 1):
        rem = m % b
        ans += arr[rem]
        for a in range(rem, n + 1, b):
            arr[a] += 1
            print(arr)
        print()
    print(ans)