# https://www.codechef.com/viewsolution/43433708

for _ in range(int(input())):
    s = input() + '0'
    groups = 0
    var = False
    for i in s:
        if int(i):
            var = True
            continue
        elif var:
            groups += 1
            var = False

    print(groups)