n = int(input())
total = 0
start = 5
for _ in range(n):
    new = (start - start%2)//2
    total += new
    start = new * 3

print(total)
