class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        lent = len(temperatures)
        sol = [0] * lent
        
        for i in range(lent - 2, -1, -1):
            j = i + 1
            while j and temperatures[j] <= temperatures[i]:
                j = (j + sol[j]) if (sol[j] > 0) else None    
            sol[i] = (j - i) if j else 0
        return sol
