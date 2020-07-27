n, s = int(input()), set(map(int, input().split()))
for _ in range(int(input())):
    op, *num = input().split()
    getattr(s, op)(*map(int, num))
print(sum(s))
