n = int(input())
s = input()

d = {'U':0, 'D':0}
count_v = 0

for step in s:
    
    if step == 'U':
        d['U'] += 1
        d['D'] -= 1
    elif step == 'D':
        d['U'] -= 1
        d['D'] += 1

    if d['U'] == 0:
        if step == 'U':
            count_v += 1

print(count_v)
