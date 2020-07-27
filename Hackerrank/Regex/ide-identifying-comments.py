import sys, re

data = sys.stdin.read()

regex = r'(/\*{1,2}.*?\*{1,2}/|//.*?(?=\n))'

for i in re.findall(regex, data, re.DOTALL):
    print(re.sub(r'\n\s+', '\n', i))
