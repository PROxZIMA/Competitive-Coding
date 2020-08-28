# https://www.codechef.com/viewsolution/36510960

for _ in range(int(input())):
    s = list(input())
    p = input()

    for i in p[1:]:
        s.remove(i)

    s = ''.join(sorted(s))

    i = s.rfind(p[0]) + 1

    print(min(s[:s.index(p[0])+1] + p[1:] + s[s.index(p[0])+1:], s[:i] + p[1:] + s[i:]))