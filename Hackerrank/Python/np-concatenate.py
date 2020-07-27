import numpy

n, m, p = input().split()

print(numpy.array([list(map(int, input().split())) for _ in range(int(n)+int(m))]))
