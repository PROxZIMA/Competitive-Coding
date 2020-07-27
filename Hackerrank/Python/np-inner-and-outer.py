import numpy
A, B = numpy.array(list(map(int, input().split()))), numpy.array(list(map(int, input().split())))
print(numpy.inner(A, B))
print(numpy.outer(A, B))
