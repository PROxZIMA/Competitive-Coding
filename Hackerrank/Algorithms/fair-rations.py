n = int(input())
b = list(map(int, input().rstrip().split()))

count = 0
total = 0
l = len(b)-1
for i in b:
    try:
        if i%2 != 0:
            b[count] += 1
            b[count + 1] += 1
            total += 1
    except:
        break
    count += 1
    
    if count == l:
        break

if b[-1]%2 == 0:
    print(total*2)
else:
    print('NO')
