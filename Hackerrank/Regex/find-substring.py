import re
n = ''
for _ in range(int(input())):
    n += input() + ' '

for _ in range(int(input())):
    s = input()
    regex = r'(?<=\w)('+s+')(?=\w)'
    print(len(re.findall(regex, n)))
