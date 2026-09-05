class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        row = len(matrix)
        column = len(matrix[0])

        left = 0
        right = row * column - 1

        while left <= right:
            mid = left + (right - left) // 2

            mid_val = matrix[mid // column][mid % column]

            if mid_val == target:
                return True
            elif mid_val > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return False