# https://www.codechef.com/viewsolution/43431995

n, h, x = map(int, input().split())

timeZones = map(int, input().split())

for time in timeZones:
    if time + x >= h:
        print('YES')
        break
else:
    print('NO')