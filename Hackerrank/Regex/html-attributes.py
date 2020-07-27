import re
from collections import defaultdict

dic = defaultdict(set)
for _ in range(int(input())):
    for tag, attr in re.findall(r'<(\w+)(.*?)?>', input()):
        dic[tag].update(re.findall(r'\s(\w+)=', attr))

for tag, attr in sorted(dic.items()):
    print(f"{tag}:{','.join(sorted(attr))}")
