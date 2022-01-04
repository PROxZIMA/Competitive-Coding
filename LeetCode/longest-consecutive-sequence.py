class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sol = 0
        maps = {}
        for elem in nums:
            if elem not in maps:
                left = maps[elem-1] if elem-1 in maps else 0
                right = maps[elem+1] if elem+1 in maps else 0
                
                score = left + right + 1
                sol = max(sol, score)
                maps[elem] = score
                maps[elem-left] = score
                maps[elem+right] = score
            print(maps)
        return sol
