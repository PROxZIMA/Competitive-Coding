import re

s = ''
for _ in range(int(input())):
    s += input().strip() + ' '


regex = r'<a href="(.*?)".*?>\s?([^<>]*?)</'

for elem in re.findall(regex, s):
    print(','.join(elem))
