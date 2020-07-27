from itertools import combinations_with_replacement as cr
word, num = input().split()
print('\n'.join(''.join(i) for i in cr(sorted(word), int(num))))
