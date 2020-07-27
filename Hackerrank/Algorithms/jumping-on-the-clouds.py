n = int(input())
c = list(map(int, input().split()))

jump = 0
count = 0
while count < n-1:
    try:
        if c[count + 2] == 0:
            count += 2
            jump += 1
        else:
            count += 1
            jump += 1
    except:
        if c[count + 1] == 0:
            count += 2
            jump += 1

print(jump)
