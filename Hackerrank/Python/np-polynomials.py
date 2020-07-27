import numpy
poly = list(map(float, input().split()))
n = int(input())
print(numpy.polyval(poly, n))
