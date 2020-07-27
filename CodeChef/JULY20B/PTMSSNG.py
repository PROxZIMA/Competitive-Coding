# https://www.codechef.com/viewsolution/35889184
x = []
y = []
xa, ya = x.append, y.append
for _ in range(int(input())):
    n = int(input())
    for _ in range(4*n-1):
        x1, y1 = map(int, input().split())
        xa(x1)
        ya(y1)
        
    resx = 0
    resy = 0
    for elem in x:
        resx = resx ^ elem 

    for elem in y:
        resy = resy ^ elem

    print(resx, resy)

    x.clear()
    y.clear()