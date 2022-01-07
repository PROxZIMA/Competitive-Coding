class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        l = len(A)
        solution = 0
        dp = [0] * l
        dp[-1] = A[-1]

        for i in range(l - 2, -1, -1):
            dp[i] = max(dp[i + 1], A[i])

        for i in range(1, l-1):
            if A[i] < dp[i+1] and 2 * A[i] - 1 + dp[i+1] > solution:
                first = -1
                for j in range(i-1, -1, -1):
                    if first < A[j] and A[j] < A[i]:
                        first = A[j]
                solution = max(solution, first + A[i] + dp[i+1])

        return solution
