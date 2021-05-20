# https://www.codechef.com/viewsolution/43859907

def factorial(a):
    if not a:
        return 1
    return a * factorial(a - 1)

for _ in range(int(input())):
    print(factorial(int(input())))