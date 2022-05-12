# https://www.codechef.com/viewsolution/69674014

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    isOne = 0
    sol = 0

    for elem in a:
        if elem == 1:
            isOne += 1
        else:
            sol += (isOne * (isOne + 1)) // 2
            isOne = 0

    sol += (isOne * (isOne + 1)) // 2
    print(sol)
