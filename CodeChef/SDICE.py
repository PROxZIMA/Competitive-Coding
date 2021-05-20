# https://www.codechef.com/viewsolution/44440549

for _ in range(int(input())):
    n = int(input())

    if n % 4 == 0:
        print(44 * (n // 4) + 16)

    else:
        k = 1
        if n // 4 == 0:
            k = 0
        if n % 4 == 1:
            print(44 * (n // 4) + 12 * k + 20) # 1 pip down

        elif n % 4 == 2:
            print(44 * (n // 4) + 8 * k  + 36) # 1-2 pip down, 2-1

        elif n % 4 == 3:
            print(44 * (n // 4) + 4 * k  + 51) # 1-2-2 pip down, 2-(1-3)-1