import re
s, r = input(), input()
m = list(re.finditer(r'(?=(%s))'%r, s))
if m:
    for i in m:
        print((i.start(), i.start()+len(r)-1))
else:
    print((-1, -1))
