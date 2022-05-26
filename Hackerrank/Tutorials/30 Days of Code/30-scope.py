class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maxDiff = 0
    def computeDifference(self):
        for i in self.__elements:
            for j in self.__elements:
                if self.maxDiff < abs(i-j):
                    self.maxDiff = abs(i-j)


_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maxDiff)