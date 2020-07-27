s = input()
t = input()
k = int(input())
lens = len(s)
lent = len(t)

count = 0
for i in range(min(lens, lent)):
    if s[i] == t[i]:
        count += 1
    else:
        break

mini = lens + lent - 2*count

if k >= lens + lent:
    print('Yes')
elif k < mini:
    print('No')
else:
    if (mini%2==0 and k%2==0) or (mini%2==1 and k%2==1):
        print('Yes')
    else:
        print('No')
