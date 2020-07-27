import re

s = ''
for _ in range(int(input())):
    s += input() + ' '

for _ in range(int(input())):
    f1 = input()
    f2 = f1.replace('our', 'or')
    regex = r'(\b'+f1+r'\b|\b'+f2+r'\b)'
    print(len(re.findall(regex, s)))
