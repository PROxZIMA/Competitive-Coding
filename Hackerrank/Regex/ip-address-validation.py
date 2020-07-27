import re

n = '([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])'
m = '[0-9a-f]{0,4}'

reip4 = r'^'+n+'(\.'+n+'){3}$'
reip6 = r'^'+m+'(:'+m+'){7}$'


for _ in range(int(input())):
    s = input()
    if re.match(reip4, s):
        print('IPv4')
    elif re.match(reip6, s):
        print('IPv6')
    else:
        print('Neither')
