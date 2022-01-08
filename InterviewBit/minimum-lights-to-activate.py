class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        l = len(A)
        pos = -1
        for i in range(0, min(B-1, l-1)+1):
            if A[i] == 1:
                pos = i
        if pos == -1:
            return -1

        requiredLights = 1

        while (pos + B - 1 < l - 1):
            currPos = pos + 1
            nextPos = -1
            while (currPos <= min(pos + 2 * B - 2 + 1, l - 1)):
                if (A[currPos] == 1):
                    nextPos = currPos
                currPos += 1

            if (nextPos == -1):
                return -1

            requiredLights += 1
            pos = nextPos

        return requiredLights
