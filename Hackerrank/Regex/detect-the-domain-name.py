import re

s = ''
for _ in range(int(input())):
    s += input() + ' '

regex = r'https?://(?:www.|ww2.)?((?:[\w-]+\.)+[a-zA-Z0-9]+)'
print(';'.join(sorted(set(re.findall(regex, s)))))
