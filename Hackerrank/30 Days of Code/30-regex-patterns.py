import re

N = int(input())
l = []

for N_itr in range(N):
    firstName, emailID = input().split()

    if re.match(r'^[a-z\.]{1,20}@gmail\.com$', emailID):
        l.append(firstName)

print('\n'.join(sorted(l)))
