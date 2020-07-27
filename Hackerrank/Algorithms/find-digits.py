t = int(input())

for _ in range(t):
    n = int(input())
    count = 0
    for i in str(n):
        try:
            if n%int(i) == 0:
                count += 1
        except:
            pass
    print(count)
