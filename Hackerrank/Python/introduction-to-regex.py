import re

regex = r'[+-]?\d*\.\d+$'

for _ in range(int(input())):
    print(bool(re.match(regex, input())))
