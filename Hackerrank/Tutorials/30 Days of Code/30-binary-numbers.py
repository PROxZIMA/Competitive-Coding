import re

n = int(input())
b = f'{n:b}'
print(len(max(re.findall(r'1+', b))))