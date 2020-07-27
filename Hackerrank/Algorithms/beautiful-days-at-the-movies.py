i, j, k = map(int, input().split())
print(sum(1 for i in range(i, j+1) if (i - int(str(i)[::-1]))%k == 0))
