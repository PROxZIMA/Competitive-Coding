import re

regex = r'([a-zA-Z0-9])\1+'

m = re.search(regex, input())

print(m.group(1) if m else -1)
