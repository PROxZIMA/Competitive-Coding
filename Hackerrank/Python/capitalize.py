def solve(s):
    return ' '.join(i.capitalize() for i in s.split(' '))

s = input()
print(solve(s))