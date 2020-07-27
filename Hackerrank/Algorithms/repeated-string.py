s = input()
n = int(input())

lens = len(s)
q = n//lens
r = n%lens

total = q*(s.count('a')) + s[:r].count('a')

print(total)
