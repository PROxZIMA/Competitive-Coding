class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        lmax, rmax = 0, 0
        water = 0
        while l <= r:
            lh, rh = height[l], height[r]
            lmax, rmax = max(lmax, lh),  max(rmax, rh)
            if lmax < rmax:
                l += 1
                water += (lmax - lh)
            else:
                r -= 1
                water += (rmax - rh)
        return water
