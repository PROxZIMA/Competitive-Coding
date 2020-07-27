l = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    l.append([name, score])
mark = sorted(list(set(i[1] for i in l)))[1]
for i in sorted(l):
    if i[1] == mark:
        print(i[0])
