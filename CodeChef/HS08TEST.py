# https://www.codechef.com/viewsolution/43722329

x, y = input().split()
x, y = int(x), float(y)

print(f'{y if x + 0.5 > y or x % 5 != 0 else y - x - 0.5:.2f}')