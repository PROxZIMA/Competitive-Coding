# https://www.codechef.com/viewsolution/36206139

for _ in range(int(input())):
    l, b = map(int, input().split())
    sl, sb = 0, 0

    x, i = True, 1
    while True:
        if x:
            sl += i
            if sl > l:
                sl -= i
                break
        else:
            sb += i
            if sb > b:
                sb -= i
                break

        i += 1
        x = not(x)

    print('Limak' if sl > sb else 'Bob')