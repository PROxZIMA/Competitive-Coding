class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        solution = [[1]]
        for j in range(numRows-1):
            old = solution[-1]
            new = [1] + [old[i] + old[i+1] for i in range(j)] + [1]
            solution.append(new)
        return solution
