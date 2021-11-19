class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area, stack = 0, [-1]
        heights.append(0)

        for i, height in enumerate(heights):
            while heights[stack[-1]] > height:
                h = heights[stack.pop()]
                area = max(area, h * (i - (stack[-1] + 1)))
            stack.append(i)
        return area
