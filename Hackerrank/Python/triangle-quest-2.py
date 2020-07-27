num = int(input())

for i in range(1, num+1):
    s = ''
    for j in range(1, i):
        s += str(j)
    for j in range(i, 0, -1):
        s += str(j)
    print(s)