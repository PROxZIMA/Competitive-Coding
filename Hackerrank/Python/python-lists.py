N = int(input())
l = []
for i in range(N):
    op, *value = input().split()
    value = list(map(int, value))
    if op == 'print':
        print(l)
    else:
        # Again not a good idea to use exec or eval
        eval(f'l.{op}{tuple(value)}')
