class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        sol = []
        i, j = 0, 0
        while i < len(A) and j < len(B):
            if A[i][1] < B[j][0]:
                i += 1
            elif B[j][1] < A[i][0]: 
                j += 1
            else:
                sol.append([max(A[i][0], B[j][0]), min(A[i][1], B[j][1])]);
                if A[i][1] < B[j][1]:
                    i += 1
                else:
                    j += 1
        return sol
