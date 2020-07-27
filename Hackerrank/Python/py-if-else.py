n = int(input())
if n%2 == 1 or (n%2 == 0 and 6<=n<=20):
    print('Weird')
elif n%2 == 0 or (2<=n<=5 and 20<n):
    print('Not Weird')
