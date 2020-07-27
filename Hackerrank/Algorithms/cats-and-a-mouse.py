q = int(input())
for _ in range(q):
    x, y, z = map(int, input().split())
    if abs(z-x)<abs(z-y):
        print('Cat A')
    elif abs(z-y)<abs(z-x):
        print('Cat B')
    else:
        print('Mouse C')
