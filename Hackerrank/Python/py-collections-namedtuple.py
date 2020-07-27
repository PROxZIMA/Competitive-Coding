from collections import namedtuple
n = int(input())
data = namedtuple('data', input().split())
print(f'{sum([int(data._make(input().split()).MARKS) for _ in range(n)])/n:.2f}')
