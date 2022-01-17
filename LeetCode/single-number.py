class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        sol = 0
        for n in nums:
            sol ^= n
        return sol
