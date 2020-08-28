# n, m = map(int, input().split())
# a = [list(map(int, list(input()))) for _ in range(n)]

n, m = 2, 2
a = [['0', '0'], ['0', '0']]

# q = int(input())
q = 3

for _ in range(q):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1 - 1, x2):
        for j in range(y1 - 1, y2):
            a[i][j] = str(1 - int(a[i][j]))

for i in range(n):
    print(''.join(a[i]))