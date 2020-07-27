import re
regex = r'#(?:[\da-f]{3}){1,2}(?!\s|{)'
s = ''
for _ in range(int(input())):
    s+=input()

print('\n'.join(re.findall(regex, s, re.I)))
