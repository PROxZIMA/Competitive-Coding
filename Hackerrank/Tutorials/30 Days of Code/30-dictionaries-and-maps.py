d = {}
n = int(input())
for _ in range(n):
    name, num = input().split()
    d[name] = num
while True:
    try:
        check = input()
        print(f'{check}={d[check]}' if d.get(check, None) != None else 'Not found')
    except EOFError:
        break
