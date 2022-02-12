# https://www.codechef.com/viewsolution/63797075

def isRainbow(n, a):
    nums = [False] * 7

    for i in range(n // 2 if n % 2 else n // 2 - 1, 0, -1):
        if not (a[i] == a[n - i - 1] and (a[i] - a[i - 1]) in {0, 1} and 0 < a[i] <= 7):
            return 'no'
        nums[a[i] - 1] = True

    if not (a[0] == a[n - 1] and 0 < a[i] <= 7):
        return 'no'

    nums[a[0] - 1] = True

    if not all(nums):
        return 'no'

    return 'yes'
    

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    print(isRainbow(n, a))
