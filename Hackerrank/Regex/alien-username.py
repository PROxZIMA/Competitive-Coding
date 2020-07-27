import re

regex = r'^[_.]\d+[a-zA-Z]*_?$'

for _ in range(int(input())):
    s = input()
    if re.match(regex, s):
        print('VALID')
    else:
        print('INVALID')
