from collections import Counter

n = int(input())
arr = list(map(int, input().split()))

maxi = max(dict(Counter(arr)).values())

print(len(arr)-maxi)
