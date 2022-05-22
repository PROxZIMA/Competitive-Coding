# https://www.codechef.com/viewsolution/71180556

for _ in range(int(input())):
    n = int(input())
    p = list(map(int, input().split()))
    print(sum(p) + max(p))
