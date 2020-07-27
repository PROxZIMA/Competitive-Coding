p, d, m, s = map(int, input().split())

count = 0
total = 0
while p >= m and total <= s:
    total += p
    p -= d
    count += 1

if p - d < m:
    while total <= s:
        total += m
        count += 1

print(count-1)
