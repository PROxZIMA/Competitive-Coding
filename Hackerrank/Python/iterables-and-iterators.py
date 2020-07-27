from itertools import combinations

n = int(input())

combi = list(combinations(input().split(), int(input())))

count = sum(1 for elem in combi if 'a' in elem)

print(count/len(combi))
