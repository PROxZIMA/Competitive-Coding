class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        index = {j: i for i, j in enumerate(nums)}

        sol = set()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                s = -(nums[i] + nums[j])
                if s in index and index[s] > j:
                    sol.add(tuple(sorted([nums[i], nums[j], s])))

        return list(sol)
