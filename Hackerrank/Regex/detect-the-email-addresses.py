import re

s = ''
for _ in range(int(input())):
    s += input() + ' '

regex = r'([\w\.]+@[\w+\.]+\.\w+)'
print(';'.join(sorted(set(re.findall(regex, s)))))
