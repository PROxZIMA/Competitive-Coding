from math import atan, degrees

a = int(input())
b = int(input())

print(str(int(round(degrees(atan(a/b)))))+'°')