class Solution:
    def maxScore(self, C: List[int], k: int) -> int:
        total = sum(C)
        factor = len(C) - k
        k_min = sum(C[:factor])
        k_curr = k_min

        for i in range(factor, len(C)):
            k_curr = k_curr - C[i - factor] + C[i]
            k_min = min(k_min, k_curr)

        return total - k_min
