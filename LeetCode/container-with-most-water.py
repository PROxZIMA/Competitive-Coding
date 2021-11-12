class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        water = 0
        while l <= r:
            lh, rh = height[l], height[r]
            if lh < rh:
                water = max(water, (r-l)*lh)
                l += 1
            else:
                water = max(water, (r-l)*rh)
                r -= 1
        return water
