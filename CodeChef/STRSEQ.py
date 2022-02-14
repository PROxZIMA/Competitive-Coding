# https://www.codechef.com/viewsolution/63833510

n = int(input())
a = list(map(int, input().split()))

def isStrict(n, a):
    if a[n - 1] > a[0]:
        for i in range(1, n):
            if a[i] <= a[i - 1]:
                return 'No'
    else:
        for i in range(1, n):
            if a[i] >= a[i - 1]:
                return 'No'
    return 'Yes'

print(isStrict(n, a))
