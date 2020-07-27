from collections import OrderedDict

fruits = OrderedDict()

for _ in range(int(input())):
    name, price = input().rsplit(' ', 1)
    fruits[name] = fruits.get(name, 0) + int(price)

for i, j in fruits.items():
    print(i, j)
