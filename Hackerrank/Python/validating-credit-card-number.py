import re
re1 = r'^[456](\d{15}|\d{3}(-\d{4}){3})$'
re2 = r'(\d)\1{3,}'

for _ in range(int(input())):
    s = input()
    if re.match(re1, s) and not re.search(re2, s.replace('-', '')):
        print('Valid')
    else:
        print('Invalid')
