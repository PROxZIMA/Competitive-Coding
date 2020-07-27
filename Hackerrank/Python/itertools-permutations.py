from itertools import permutations

word, num = input().split()
print('\n'.join(''.join(i) for i in sorted(permutations(word, int(num)))))
