m, mset = int(input()), set(map(int, input().split()))
n, nset = int(input()), set(map(int, input().split()))

for i in sorted(list(mset-nset) + list(nset-mset)):
    print(i)
