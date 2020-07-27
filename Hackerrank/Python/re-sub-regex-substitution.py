import re

for _ in range(int(input())):
    print(re.sub('(?<= )\|\|(?= )', 'or', re.sub('(?<= )\&\&(?= )', 'and', input())))
