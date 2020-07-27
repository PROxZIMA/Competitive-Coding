import numpy

def arrays(arr):
    return numpy.array(list(reversed(arr)), float)

arr = list(map(int, input().split()))
print(arrays(arr))