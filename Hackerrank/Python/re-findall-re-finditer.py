import re
regex = r'[qwrtypsdfghjklzxcvbnm]([aeiou]{2,})(?=[qwrtypsdfghjklzxcvbnm])'
print('\n'.join(re.findall(regex, input(), re.I) or ['-1']))
