import re
for _ in range(int(input())):
    s = input()
    if s == 'hackerrank':
        print(0)
    elif re.search(r'hackerrank$', s):
        print(2)
    elif re.search(r'^hackerrank', s):
        print(1)
    else:
        print(-1)
