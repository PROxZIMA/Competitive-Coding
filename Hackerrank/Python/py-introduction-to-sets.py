def average(array, l):
    return sum(array)/l

l = int(input())
arr = set(map(int, input().split()))
print(average(arr, l))