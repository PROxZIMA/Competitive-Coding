# https://www.codechef.com/viewsolution/44049932

arr = tuple(i**2 for i in range(1, 1001))

for _ in range(int(input())):
    for num in arr:
        print(num)
        if int(input()):
            break