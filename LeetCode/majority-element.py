class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maxi, counter = nums[0], 0
        for elem in nums:
            if maxi == elem:
                counter += 1
            elif counter == 0:
                maxi = elem
                counter += 1
            else:
                counter -= 1
        return maxi
