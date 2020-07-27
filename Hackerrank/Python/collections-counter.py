from collections import Counter

lens, sizes = int(input()), Counter(map(int, input().split()))
total = 0

for _ in range(int(input())):
    size, cost = map(int, input().split())
    if (size in sizes.keys()) and (sizes[size]!=0):
        sizes[size]-=1
        total += cost

print(total)
