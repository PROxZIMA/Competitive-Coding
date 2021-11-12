from math import inf

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        mini = inf
        prevSum = 0
        for i in range(len(nums)):
            nums[i] += prevSum
            prevSum = nums[i]
            if mini > prevSum:
                mini = prevSum

        return 1 if mini > 0 else abs(mini) + 1
