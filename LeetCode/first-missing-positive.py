class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        lenn = len(nums)

        for i in range(lenn):
            if nums[i] < 0 or lenn < nums[i]:
                nums[i] = 0

        for i in nums:
            rem = i % (lenn + 1)
            if 0 < rem <= lenn:
                nums[rem - 1] += (lenn + 1)

        for i in range(lenn):
            if nums[i] // (lenn + 1) == 0:
                return i + 1

        return lenn + 1
