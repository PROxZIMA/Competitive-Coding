import re
lo = '(\d(\.\d+)?|[1-8]\d(\.\d+)?|90(\.0+)?)'
la = '(\d(\.\d+)?|[1-9]\d(\.\d+)?|1[0-7]\d(\.\d+)?|180(\.0+)?)'
regex = f'^\([+-]?{lo}, [+-]?{la}\)$'

for _ in range(int(input())):
    if re.match(regex, input()):
        print('Valid')
    else:
        print('Invalid')
