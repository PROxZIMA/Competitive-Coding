class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        isColZero, rows, columns = False, len(matrix), len(matrix[0])
        
        for i in range(rows):
            isColZero = isColZero or matrix[i][0] == 0
            for j in range(1, columns):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(rows - 1, -1, -1):
            for j in range(columns - 1, 0, -1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            if isColZero:
                matrix[i][0] = 0
