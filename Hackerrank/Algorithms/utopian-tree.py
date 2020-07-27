t = int(input())

for t_itr in range(t):
    n = int(input())
    count = 0
    for i in range(n+1):
        if i%2 == 0:
            count+=1
        else:
            count*=2
    print(count)
