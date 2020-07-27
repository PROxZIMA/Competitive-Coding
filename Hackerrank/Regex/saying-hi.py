import re
regex = r'[Hh][Ii]\s[^Dd]'
for _ in range(int(input())):
    s = input()
    if re.match(regex, s):
        print(s)
