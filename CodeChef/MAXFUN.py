# https://www.codechef.com/viewsolution/42321521

for _ in range(int(input())):
    n = int(input())
    arr = sorted(map(int, input().split()))
    print((arr[-1] - arr[0])*2)