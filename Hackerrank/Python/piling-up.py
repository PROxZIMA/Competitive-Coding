from collections import deque

for _ in range(int(input())):
    t, side = input(), list(map(int, input().split()))
    num = max(side[0], side[-1])
    while True:
        try:
            if (side[0] >= side[-1]) and (side[0] <= num):
                num = side.pop(0)
            elif (side[0] < side[-1]) and (side[-1] <= num):
                num = side.pop(-1)
            else:
                print('No')
                break
        except IndexError:
            break

    if side == []: print('Yes')
        
