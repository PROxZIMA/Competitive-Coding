seta, n = set(input().split()), int(input())
l = []
for i in range(n):
    l.append(seta.issuperset(set(input().split())))
print(all(l))
