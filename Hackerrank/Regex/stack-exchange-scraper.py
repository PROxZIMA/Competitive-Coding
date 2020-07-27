import re, sys

frag = sys.stdin.read()

regex = r'(?<=/questions/)(\d+?)(?=/).+?(?<="question-hyperlink">)(.+?)(?=<).+?(?<="relativetime">)(.+?)(?=<)'

for elem in re.findall(regex, frag, re.DOTALL):
    print(';'.join(elem))
