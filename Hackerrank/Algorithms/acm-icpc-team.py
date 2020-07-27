from itertools import combinations

n, m = map(int, input().split())

values = []
for _ in range(n):
    att = input()
    a = set(filter(lambda x: att[x] == '1', range(len(att))))
    values.append(a)

maxi = 0
tot_lst = []
for x, y in combinations(values, 2):
    l = len(x|y)
    if l > maxi:
        maxi = l
    tot_lst.append(l)

total = sum(1 for x in tot_lst if x == maxi)

print(maxi)
print(total)
