class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        rem_freq = [0] * k
        rem_freq[0] = 1
        total = ans = 0

        for num in nums:
            total = (total + num) % k
            ans += rem_freq[total]
            rem_freq[total] += 1

        return ans
