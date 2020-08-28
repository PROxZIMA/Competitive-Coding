# https://www.codechef.com/viewsolution/36973732

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if a[i] & a[j] == a[i]:
                count += 1
    
    print(count)