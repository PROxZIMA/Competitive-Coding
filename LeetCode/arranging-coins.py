from math import sqrt

class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int(sqrt(2) * sqrt(n + 1) + 0.5) - 1
