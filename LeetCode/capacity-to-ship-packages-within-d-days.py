class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        while left < right:
            mid, daysRequired, weightPerDay = (left + right) // 2, 1, 0
            for weight in weights:
                if weightPerDay + weight > mid:
                    daysRequired += 1
                    weightPerDay = 0
                weightPerDay += weight

            if daysRequired > days:
                left = mid + 1
            else:
                right = mid
        return left
