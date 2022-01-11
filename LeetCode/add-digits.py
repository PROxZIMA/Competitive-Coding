class Solution:
    def addDigits(self, num: int) -> int:
        if not num: return 0
        return (num - 1) % 9 + 1
