from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        prefixSum = 0
        sumCount = defaultdict(int)

        for num in nums:
            prefixSum += num

            if prefixSum == k:
                ans += 1
            if prefixSum - k in sumCount:
                ans += sumCount[prefixSum - k]

            sumCount[prefixSum] += 1
            print(sumCount)

        return ans
