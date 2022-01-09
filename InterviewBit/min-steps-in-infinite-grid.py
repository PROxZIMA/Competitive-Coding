class Solution:
	# @param A : list of integers
	# @param B : list of integers
	# @return an integer
	def coverPoints(self, A, B):
        x1, y1 = A[0], B[0]
        steps = 0
        for i in range(1, len(A)):
            x2, y2 = A[i], B[i]
            steps += max(abs(y2 - y1), abs(x2 - x1))
            x1, y1 = x2, y2
        return steps
