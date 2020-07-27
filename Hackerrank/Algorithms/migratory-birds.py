
arr_count = input()

arr = map(int, input().split())

l = [0, 0, 0, 0, 0, 0]

for i in arr:
    l[i] += 1

print(l.index(max(l)))
