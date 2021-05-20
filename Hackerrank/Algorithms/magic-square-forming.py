ms1 = [8, 1, 6,
       3, 5, 7,
       4, 9, 2]

ms2 = [6, 7, 2,
       1, 5, 9,
       8, 3, 4]

ms3 = [2, 9, 4,
       7, 5, 3,
       6, 1, 8]

ms4 = [4, 3, 8,
       9, 5, 1,
       2, 7, 6]

ms5 = [6, 1, 8,
       7, 5, 3,
       2, 9, 4]

ms6 = [8, 3, 4,
       1, 5, 9,
       6, 7, 2]

ms7 = [4, 9, 2,
       3, 5, 7,
       8, 1, 6]

ms8 = [2, 7, 6,
       9, 5, 1,
       4, 3, 8]

def sub(l1, l2):
    return sum(abs(i - j) for i, j in zip(l1, l2))

check = []
for _ in range(3):
    check.extend(list(map(int, input().split())))

print(min(sub(ms1, check),
          sub(ms2, check),
          sub(ms3, check),
          sub(ms4, check),
          sub(ms5, check),
          sub(ms6, check),
          sub(ms7, check),
          sub(ms8, check)))