import re

s = ''
for _ in range(int(input())):
    s += input() + ' '

for _ in range(int(input())):
    f = input()
    regex = r'(\b'+f[:-2]+r'ze\b|\b'+f[:-2]+r'se\b)'
    print(len(re.findall(regex, s)))
