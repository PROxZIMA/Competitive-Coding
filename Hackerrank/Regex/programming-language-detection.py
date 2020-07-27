import sys

data = sys.stdin.read()

if '#include' in data:
    print('C')
elif 'import java' in data:
    print('Java')
else:
    print('Python')
