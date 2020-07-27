import numpy
n, m = input().split()
myarr = numpy.array([list(map(int, input().split())) for _ in range(int(n))])
print(numpy.transpose(myarr))
print(myarr.flatten())
