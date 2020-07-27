import re

s = ''
for _ in range(int(input())):
    s += input() + ' '

for _ in range(int(input())):
    f = input()
    regex = r'(?:(?<=[\W])|^)('+f+r')(?:(?=[\W])|$)'
    print(len(re.findall(regex, s)))
