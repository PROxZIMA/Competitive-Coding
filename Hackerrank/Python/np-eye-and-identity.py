import numpy
n, m = input().split()
print(str(numpy.eye(int(n), int(m))).replace('1', ' 1').replace('0', ' 0'))
