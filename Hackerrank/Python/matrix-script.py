import re

n, m = map(int, input().split())
s = ''.join([''.join(list(i)) for i in zip(*[input() for _ in range(n)])])

print(re.sub(r'(?<=[\w])[!@#$%&\s]+(?=[\w])', ' ', s))
