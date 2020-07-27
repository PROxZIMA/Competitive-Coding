from collections import Counter

n = int(input())
ar = map(int, input().split())

total = dict(Counter(ar))
print(sum((v-v%2)//2 for k, v in total.items()))
