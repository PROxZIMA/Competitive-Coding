class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        solution = [intervals[0]]
        for k in range(1, len(intervals)):
            i, j = solution[-1]
            x, y = intervals[k]
            if i == x or x <= j:
                solution[-1][-1] = max(j, y)
            else:
                solution.append(intervals[k])
        return solution
