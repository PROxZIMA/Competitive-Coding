import numpy
n, m = input().split()
arr = numpy.array([list(map(int, input().split())) for _ in range(int(n))])
print(numpy.max(numpy.min(arr, axis = 1)))
