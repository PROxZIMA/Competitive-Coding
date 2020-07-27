t = int(input())
for t_itr in range(t):
    n, k = map(int, input().split())
    l = list(filter(lambda x: x<=0, map(int, input().split())))
    if len(l) >= k:
        print('NO')
    else:
        print('YES')
