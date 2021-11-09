class Solution:
    def numTrees(self, n: int) -> int:
        # Possible BST with n keys = 2nCn/(n+1) = 2n!/((n+1)!*n!)
        return self.binomialCoeff(2 * n, n) // (n + 1)

    def binomialCoeff(self, n, k):
        res = 1
        if (k > n - k):
            k = n - k

        for i in range(k):
            res *= (n - i)
            res //= (i + 1)

        return res
