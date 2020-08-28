def fibo(n):
    a = 0
    b = 1
    while a+b <= n:
        a, b = b, a+b
        yield b

for _ in range(int(input())):
    n = int(input())
    print(sum(i for i in fibo(n) if i%2==0))