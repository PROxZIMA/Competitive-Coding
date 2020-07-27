import re
regex = r'^[A-Z]{5}\d{4}[A-Z]$'
for _ in range(int(input())):
    if re.match(regex, input()):
        print('YES')
    else:
        print('NO')
