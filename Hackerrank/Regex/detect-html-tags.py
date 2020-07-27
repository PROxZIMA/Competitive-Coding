import re

s = ''

for _ in range(int(input())):
    s += input()

regex = r'<\s*(\w+)'

print(';'.join(sorted(set(re.findall(regex, s)))))
