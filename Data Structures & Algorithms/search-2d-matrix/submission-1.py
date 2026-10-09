class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # calculate the rows in 2D representation of the matrix
        rows = len(matrix)
        # cal the cols in matrics
        cols = len(matrix[0])
        # left will always start from 0 index
        left = 0
        # right here will be the total elements in matrics  - 1 for index
        right = (rows * cols) - 1

        while left <= right:
            mid = (left + right) // 2
            
            row = mid // cols
            col = mid % cols
            
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False