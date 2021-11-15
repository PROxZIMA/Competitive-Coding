class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k, lenn = 1, len(nums)
        if lenn < 2:
            return lenn
        for i in range(lenn - 1):
            if (nums[i]!=nums[i + 1]):
                nums[k] = nums[i + 1]
                k += 1
        return k
