for _ in range(int(input())):
    n = int(input())
    ssq = ((n * (n + 1)) // 2) ** 2
    sqs = (n * (n + 1) * (2 * n + 1)) // 6
    print(ssq - sqs)