import re

for _ in range(int(input())):
    uid = input()
    print('Invalid' if not uid.isalnum() or len(uid) != 10 or len(set(uid)) != len(uid) or len(re.findall(r'[A-Z]', uid)) < 2 or len(re.findall(r'\d', uid)) < 3 else 'Valid')
    