class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums2 = [target - i for i in nums]
        x = list(set(nums) & set(nums2))[0]
        y = target - x
        
        return sorted([i for i in range(len(nums)) if nums[i] == x or nums[i] == y])

        # Hashmap Solution
        maps = dict()
        for x, y in enumerate(nums):
            if target-y in maps:
                return [maps[target-y], x]
            maps[y] = x
