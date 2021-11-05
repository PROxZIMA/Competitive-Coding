class Solution:
    def convert(self, s: str, n: int) -> str:
        if n == 1:
            return s
        lens = len(s)
        sol, arr = [], []

        for i in range(0, lens + 2*n-2, 2*n-2):
            arr.append(i)
            try:
                sol.append(s[i])
            except:
                pass

        for i in range(1, n-1):
            for j in arr:
                x, y = j - i, j + i
                if 0 <= x < lens:
                    sol.append(s[x])
                if 0 <= y < lens:
                    sol.append(s[y])

        for i in range(n - 1, len(s), 2*n-2):
            sol.append(s[i])

        return ''.join(sol)
