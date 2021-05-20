n, m = map(int, input().split())
pos = [tuple(map(int, input().split())) for _ in range(n)]
seg = [list(map(int, input().split())) for _ in range(m)]

for i in range(m):
    if seg[i][2] < seg[i][0]:
        seg[i][2], seg[i][0] = seg[i][0], seg[i][2]
        seg[i][3], seg[i][1] = seg[i][1], seg[i][3]
    if i % 2:
        print(f'{1000001 - seg[i][0]} {1000000 - seg[i][1]}')
    else:
        print(f'{-seg[i][0]} {-seg[i][1] - 1}')
