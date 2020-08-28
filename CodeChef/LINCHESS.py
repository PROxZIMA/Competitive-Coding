# https://www.codechef.com/viewsolution/36399404

for _ in range(int(input())):
    n, k = map(int, input().split())
    p = map(int, input().split())
    mini = k
    v = -1
    for i in p:
        if k % i == 0 and mini > (k // i) - 1:
            mini = (k // i) - 1
            v = i
            
    print(v)