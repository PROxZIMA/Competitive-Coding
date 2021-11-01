class Solution:
    def longestValidParentheses(self, s: str) -> int:
        index = [-1]
        
        sol = 0
        for i, char in enumerate(s):
            if char == '(':
                index.append(i)
            else:
                if len(index) == 1:
                    index = [i]
                    continue
                index.pop()
                sol = max(sol, i-index[-1])

        return sol
