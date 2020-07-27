import email.utils
import re
regex = r'^[a-z0-9][a-z0-9.\-_]+@[a-z]+\.[a-z]{1,3}$'
for _ in range(int(input())):
    addr = input()
    emails = email.utils.parseaddr(addr)[1]
    if re.match(regex, emails, re.I): print(addr)
