class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        tortoise = nums[0]
        hare = nums[0]

        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]

            if hare == tortoise:
                break

        p1 = nums[0]
        p2 = tortoise

        while p1 != p2:
            p1 = nums[p1]
            p2 = nums[p2]

        return p1
