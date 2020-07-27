count = {}

for _ in range(int(input())):
    s= input()
    count[s] = count.get(s, 0) + 1

print(len(count))
print(' '.join(map(str, count.values())))
