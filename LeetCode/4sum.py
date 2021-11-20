from collections import defaultdict

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        lenn = len(nums)
        index = {j: i for i, j in enumerate(nums)}

        sol = set()
        for i in range(lenn):
            for j in range(i + 1, lenn):
                for k in range(j + 1, lenn):
                    s = target - (nums[i] + nums[j] + nums[k])
                    if s in index and index[s] > k:
                        sol.add(tuple(sorted((nums[i], nums[j], nums[k], s))))

        return list(sol)
