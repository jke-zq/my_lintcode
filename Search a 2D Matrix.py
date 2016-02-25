class Solution:
    """
    @param matrix, a list of lists of integers
    @param target, an integer
    @return a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        # if not matrix or not matrix[0]:
        #     return False
        
        # left, right = 0, len(matrix) - 1
        # while left + 1 < right:
        #     mid = left + (right - left) / 2
        #     if matrix[mid][0] > target:
        #         right = mid
        #     elif matrix[mid][0] < target:
        #         left = mid
        #     else:
        #         return True
        # if matrix[left][0] > target:
        #     return False
        # elif matrix[left][0] == target:
        #     return True
        # if matrix[right][0] == target:
        #     return True
 
        
        # row = left
        # if matrix[right][0] < target:
        #     row = right
        # left, right = 0, len(matrix[row]) - 1
        # while left + 1 < right:
        #     mid = left + (right - left) / 2
        #     if matrix[row][mid] > target:
        #         right = mid
        #     elif matrix[row][mid] < target:
        #         left = mid
        #     else:
        #         return True
        # if target in (matrix[row][left], matrix[row][right]):
        #     return True
        # return False
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        while left + 1 < right:
            mid = left + (right - left) / 2
            x, y = mid / n, mid % n
            if matrix[x][y] > target:
                right = mid
            elif matrix[x][y] < target:
                left = mid
            else:
                return True
        x, y = left / n, left % n
        if matrix[x][y] == target:
            return True
        x, y = right / n, right % n
        if matrix[x][y] == target:
            return True
        return False
        
            