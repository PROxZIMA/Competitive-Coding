# https://www.codechef.com/viewsolution/37748224

for _ in range(int(input())):
    n, k = map(int, input().split())
    binary_string = input()

    ones = 0
    for i in binary_string:
        ones += 1 & int(i)
    zeros = n - ones

    strk = n//k
    str2k = '0'*(zeros//strk) + '1'*(ones//strk)

    if zeros//strk + ones//strk == k:
        print(((str2k + str2k[::-1])*(strk//2+1))[:n])
    else:
        print('IMPOSSIBLE')