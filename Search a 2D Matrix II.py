class Solution:
    """
    @param matrix: An list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicates the total occurrence of target in the given matrix
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        left, right = 0, n - 1
        while left + 1 < right:
            mid = left + (right - left) / 2
            if matrix[m - 1][mid] < target:
                left = mid
            else:
                right = mid
        
        row, col = m - 1, right
        if matrix[m - 1][left] >= target:
            col = left
        
        ret = 0
        while row >= 0 and col < n:
            if matrix[row][col] == target:
                ret += 1
                row -= 1
                col += 1
            elif matrix[row][col] > target:
                row -= 1
            else:
                col += 1
        return ret
        