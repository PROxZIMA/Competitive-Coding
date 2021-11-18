class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        lenn = len(nums)
        sol = nums[0] + nums[1] + nums[2]
        for i in range(lenn-2):
            left, right = i + 1, lenn - 1
            while left < right:
                newSum = nums[i] + nums[left] + nums[right]
                if abs(newSum - target) < abs(sol - target):
                    sol = newSum
                if newSum < target:
                    left += 1
                elif newSum > target:
                    right -= 1
                else:
                    return target
        return sol
