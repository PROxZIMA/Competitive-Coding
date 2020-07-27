import re
regex = r'(\d{0,3})[\-\s](\d{0,3})[\-\s](\d{4,10})'
for _ in range(int(input())):
    s = input()
    code = re.findall(regex, s)
    if code:
        print(f'CountryCode={code[0][0]},LocalAreaCode={code[0][1]},Number={code[0][2]}')
