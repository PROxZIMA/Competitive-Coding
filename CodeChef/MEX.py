for _ in range(int(input())):
    n, k = map(int, input().split())
    s = set(map(int, input().split()))
    mex = 0
    while True:
        if mex not in s:
            if k:
                k -= 1
            else:
                print(mex)
                break
        mex += 1
