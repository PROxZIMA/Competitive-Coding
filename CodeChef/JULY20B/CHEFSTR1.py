# https://www.codechef.com/viewsolution/35848974
for i in range(int(input())):
    n, s = int(input()), list(map(int, input().split()))
    tot = 0
    for i in range(n-1):
        tot += abs(s[i+1] - s[i])
    print(tot - n + 1)