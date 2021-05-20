# https://www.codechef.com/viewsolution/43726268

def factorial(a):
    if a == 0:
        return 1
    return a * factorial(a - 1)

for _ in range(int(input())):
    a = int(input())
    print(factorial(a))