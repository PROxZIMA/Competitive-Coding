class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        if startPos[0] < homePos[0]:
            rStart = startPos[0] + 1
            rEnd = homePos[0] + 1
        else:
            rStart = homePos[0]
            rEnd = startPos[0]
            
        if startPos[1] < homePos[1]:
            cStart = startPos[1] + 1
            cEnd = homePos[1] + 1
        else:
            cStart = homePos[1]
            cEnd = startPos[1]

        return sum(rowCosts[rStart: rEnd]) + sum(colCosts[cStart: cEnd])
