import re
regex = r'^[789]\d{9}$'
for _ in range(int(input())):
    print('YES' if re.match(regex, input()) else 'NO')
