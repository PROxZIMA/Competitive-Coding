t = int(input())

for t_itr in range(t):
    n, m, s = map(int, input().split())
    ans = (s+m-1)%n
    if ans == 0:
        print(n)
    else:
        print(ans)
