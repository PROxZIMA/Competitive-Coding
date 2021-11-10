class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        sLen, pLen = len(s), len(p)

        dp: list[int, int] = [[0] * (pLen+1) for _ in range(sLen+1)]
        dp[0][0] = 1

        for j in range(1, pLen+1):
            if p[j-1] == '*' and dp[0][j-1]:
                dp[0][j] = 1

        for i in range(1, sLen+1):
            for j in range(1, pLen+1):
                sc, pc = s[i-1], p[j-1]

                if sc == pc or pc == '?':
                    dp[i][j] = dp[i-1][j-1]
                if pc == '*':
                    dp[i][j] = dp[i][j-1] or dp[i-1][j-1] or dp[i-1][j]

        return dp[sLen][pLen]
