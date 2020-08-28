# https://www.codechef.com/viewsolution/36397549

for _ in range(int(input())):
    h, t = list(map(int, input().split()))
    print(0 if h>=2*t else 1)