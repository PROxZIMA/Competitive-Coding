class Solution:
    def countAndSay(self, n: int) -> str:
        ans = '1 '

        for i in range(n - 1):
            temp = ''
            val = ''
            count = 1
            for j in range(len(ans) - 1):
                val = ans[j]
                if ans[j] == ans[j + 1]:
                    count += 1
                else:
                    temp += f'{count}{val}'
                    count = 1
            ans = temp + ' '

        return ans.strip()
