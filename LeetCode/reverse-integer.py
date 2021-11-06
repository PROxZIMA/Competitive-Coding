class Solution:
    def reverse(self, x: int) -> int:
        y = int(str(x)[:0:-1]) if x < 0 else int(str(x)[::-1])
        if abs(y) <= 0x7FFFFFFF:
            return y if x > 0 else -y
        else:
            return 0
