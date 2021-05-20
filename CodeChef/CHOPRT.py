# https://www.codechef.com/viewsolution/43860074

for _ in range(int(input())):
    a, b = map(int, input().split())
    print('<' if a < b else '>' if a > b else '=')