class Solution:
    def binary_search(self, arr: List[int], x: int) -> bool:
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = (high + low) // 2
            if arr[mid] < x:
                low = mid + 1
            elif arr[mid] > x:
                high = mid - 1
            else:
                return True
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low, high = 0, len(matrix) - 1
        n = len(matrix[0]) - 1
        while low <= high:
            mid = (high + low) // 2
            if matrix[mid][n] < target:
                low = mid + 1
            elif target < matrix[mid][0]:
                high = mid - 1
            else:
                return self.binary_search(matrix[mid], target)
        return False
