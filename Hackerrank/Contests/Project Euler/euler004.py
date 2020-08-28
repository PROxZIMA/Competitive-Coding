s = set()
for i in range(999, 102, -1):
    for j in range(999, 102, -1):
        n = str(i*j)
        if n == n[::-1]:
            s.add(int(n))
s = sorted(s, reverse=True)

for _ in range(int(input())):
    n = int(input())
    for i in s:
        if i < n:
            print(i)
            break
