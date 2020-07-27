n, k = map(int, input().split())
height = map(int, input().split())

jump = max(height) - k

if jump >= 0:
    print(jump)
else:
    print(0)
