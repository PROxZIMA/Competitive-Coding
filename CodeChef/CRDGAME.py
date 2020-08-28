# https://www.codechef.com/viewsolution/35855472

for _ in range(int(input())):
    c_score = 0
    m_score = 0

    for _ in range(int(input())):
        chef, morty = input().split()
        chef = sum(int(i) for i in chef)
        morty = sum(int(i) for i in morty)

        if chef > morty:
            c_score += 1
        elif morty > chef:
            m_score += 1
        else:
            c_score += 1
            m_score += 1

    if c_score > m_score: print(f'0 {c_score}')
    elif m_score > c_score: print(f'1 {m_score}')
    else: print(f'2 {m_score}')