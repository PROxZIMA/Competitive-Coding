class Solution:
    def __init__(self):
        self.nums = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}

    def pprint(self, board: List[List[str]]) -> None:
        for row in board:
            print(row)

    def checkRow(self, board: List[List[str]], i: int) -> set:
        return {num for num in board[i] if num.isdecimal()}

    def checkColumn(self, board: List[List[str]], i: int) -> set:
        return {row[i] for row in board if row[i].isdecimal()}

    def checkBox(self, board: List[List[str]], i: int, j: int) -> set:
        i, j = i // 3 * 3, j // 3 * 3
        return {board[row][col] for row in range(i, i + 3) for col in range(j, j + 3) if board[row][col].isdecimal()}

    def missingMap(self, board: List[List[str]]) -> dict:
        missingMap = {}
        for i in range(9):
            for j in range(9):
                if not board[i][j].isdecimal():
                    missingMap[f'{i}{j}'] = self.nums - (self.checkRow(board, i) | self.checkColumn(board, j) | self.checkBox(board, i, j))
        return missingMap

    def removeRCBDuplicates(self, board: List[List[str]], missingMap: dict, key: str) -> dict:
        i, j = map(int, list(key))
        val = missingMap.pop(key)
        (val,) = val
        newMissingMap = missingMap.copy()
        for nkey in missingMap:
            newi, newj = map(int, list(nkey))
            if (newi == i) or \
               (newj == j) or \
               (i // 3 == newi // 3 and j // 3 == newj // 3):
                newMissingMap[nkey].discard(val)
        return newMissingMap

    def nakedCandidates(self, board: List[List[str]], missingMap: dict) -> dict:
        newMissingMap = missingMap.copy()
        for key, value in missingMap.items():
            i, j = map(int, list(key))
            valBox = value.copy()
            valRow = value.copy()
            valCol = value.copy()

            for nkey, nvalue in missingMap.items():
                newi, newj = map(int, list(nkey))
                if i // 3 == newi // 3 and j // 3 == newj // 3 and (i != newi or j != newj):
                    valBox -= nvalue
                if (newi == i and newj != j):
                    valRow -= nvalue
                if (newj == j and newi != i):
                    valCol -= nvalue

            if len(valBox) == 1:
                newMissingMap[key] = valBox
            elif len(valRow) == 1:
                newMissingMap[key] = valRow
            elif len(valCol) == 1:
                newMissingMap[key] = valCol
        return newMissingMap

    def isValid(self, board: List[List[str]], i: int, j: int, char: str) -> bool:
        for l in range(9):
            if board[i][l] == char or board[l][j] == char:
                return False
        i, j = i // 3 * 3, j // 3 * 3

        for l in range(i, i + 3):
            for m in range(j, j + 3):
                if board[l][m] == char:
                    return False
        return True

    def solve(self, board: List[List[str]]) -> bool:
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for char in '123456789':
                        if self.isValid(board, i, j, char):
                            board[i][j] = char
                            if self.solve(board):
                                return True
                            board[i][j] = '.'
                    return False
        return True

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        missingMap = self.missingMap(board)

        while missingMap:
            newMissingMap = missingMap.copy()
            for key, value in missingMap.items():
                i, j = map(int, list(key))
                if len(value) == 1:
                    (sol,) = value
                    board[i][j] = sol
                    newMissingMap = self.removeRCBDuplicates(board, newMissingMap, key)
            if missingMap == newMissingMap:
                newMissingMap = self.nakedCandidates(board, newMissingMap)
            if missingMap == newMissingMap:
                break
            missingMap = newMissingMap.copy()
        self.solve(board)
