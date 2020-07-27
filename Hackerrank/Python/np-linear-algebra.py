import numpy
from numpy.linalg import det
n = int(input())
arr = numpy.array([list(map(float, input().split())) for _ in range(n)])
print(round(det(arr), 2))
