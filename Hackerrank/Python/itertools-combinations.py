from itertools import combinations
word, num = input().split()

for i in range(1, int(num)+1):
    print('\n'.join(''.join(i) for i in sorted(combinations(sorted(word), i))))
