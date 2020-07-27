import numpy
n = int(input())
a = numpy.array([list(map(int, input().split())) for _ in range(int(n))])
b = numpy.array([list(map(int, input().split())) for _ in range(int(n))])
print(numpy.dot(a, b))
