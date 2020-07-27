dld = '.|.'
dash = '-'

n, m = map(int, input().split())

for i in range((n-1)//2):
    print((dld*i).rjust((m-3)//2, dash)+dld+(dld*i).ljust((m-3)//2, dash))

print('WELCOME'.center(m, dash))

for i in range((n-1)//2-1, -1, -1):
    print((dld*i).rjust((m-3)//2, dash)+dld+(dld*i).ljust((m-3)//2, dash))