for _ in range(int(input())):
    n = int(input())
    print(sum(i for i in map(int, list(str(2**n)))))