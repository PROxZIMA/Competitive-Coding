# https://www.codechef.com/viewsolution/63830020

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans, temp = 0, 0

    for num in a:
        if not num % 2:
            temp += 1
        else:
            ans = max(ans, temp)
            temp = 0

    ans = max(ans, temp)
    print(ans)
