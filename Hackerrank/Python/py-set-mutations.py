len_a = int(input())
elem_a = input()
num = int(input())

A = set()
A.update(map(int, elem_a.split()))

for i in range(num):
    op = input().split()[0]
    elem = input().split()

    # This is generally a wrong idea to use but it can work here :)
    eval(f'A.{op}(map(int, {elem}))')

print(sum(A))
