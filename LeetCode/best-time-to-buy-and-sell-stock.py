class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        mini = float('inf')
        for price in prices:
            ans = max(ans, price - mini)
            mini = min(mini, price)
        return ans
