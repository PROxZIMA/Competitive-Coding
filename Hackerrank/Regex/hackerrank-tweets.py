import re

num = 0

for _ in range(int(input())):
    if re.search(r'[Hh][Aa][Cc][Kk][Ee][Rr][Rr][Aa][Nn][Kk]', input()):
        num += 1

print(num)
