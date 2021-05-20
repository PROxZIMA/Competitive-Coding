# https://www.codechef.com/viewsolution/46263290

def solution(xbit: int, obit: int) -> int:
    xint, oint = int(xbit, 2), int(obit, 2)
    xWon, oWon = won(xint, oint)
    xCount, oCount = xbit.count('1'), obit.count('1')

    if (xWon and oWon) or (not (xCount - 1 <= oCount <= xCount)):
        return 3

    if (xWon and oCount == xCount) or (oWon and oCount == xCount - 1):
        return 3

    if (((xint | oint) == 511) and (not (xWon ^ oWon))) or (xWon ^ oWon):
        return 1

    if (xint | oint) != 511:
        return 2

# winCombs = [000000111, 000111000, 111000000, 100100100, 010010010, 001001001, 100010001, 001010100]
winCombs = [7, 56, 448, 292, 146, 73, 273, 84]

def won(xint: int, oint: int) -> (bool, bool):
    xWon, oWon = False, False
    for comb in winCombs:
        if xint & comb == comb:
            xWon = True
            break
    for comb in winCombs:
        if oint & comb == comb:
            oWon = True
            break

    return (xWon, oWon)


for _ in range(int(input())):
    ttc = [input() for i in range(3)]
    grid = ''.join(ttc)
    xbit = ''.join('1' if x == 'X' else '0' for x in grid)
    obit = ''.join('1' if o == 'O' else '0' for o in grid)
    print(solution(xbit, obit))