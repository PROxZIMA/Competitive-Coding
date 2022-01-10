class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        sol = sum(A[i] for i in range(B))
        tempSol = sol
        l = len(A)
        for i in range(B):
            tempSol -= A[B - i - 1]
            tempSol += A[l - i - 1]
            sol = max(tempSol, sol)
        return sol
