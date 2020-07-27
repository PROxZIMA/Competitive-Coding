n, x = map(int, input().split())
a = [list(map(float, input().split())) for _ in range(x)]
for i in zip(*a):
    print(f'{sum(i)/x:.1f}')
