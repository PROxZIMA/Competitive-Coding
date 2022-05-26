n = int(input())

print('Weird' if (n % 2 != 0 or (n % 2 == 0 and 6 <= n <= 20)) else 'Not Weird')