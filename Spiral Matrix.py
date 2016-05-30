class Solution:
    # @param {int[][]} matrix a matrix of m x n elements
    # @return {int[]} an integer array
    def spiralOrder(self, matrix):
        # Write your code here
        def helper(rows, cols, ans, matrix):
            up, down = 0, rows - 1
            left, right = 0, cols - 1
            while up < down and left < right:
                for c in range(left, right + 1):
                    ans.append(matrix[up][c])
                for r in range(up + 1, down + 1):
                    ans.append(matrix[r][right])
                for c in range(right - 1, left - 1, -1):
                    ans.append(matrix[down][c])
                for r in range(down - 1, up, -1):
                    ans.append(matrix[r][left])
                up += 1
                down -= 1
                left += 1
                right -= 1
            if left == right:
                for r in range(up, down + 1):
                    ans.append(matrix[r][left])
            # error. not if, but elif
            elif up == down:
                for c in range(left, right + 1):
                    ans.append(matrix[up][c])
            return ans
        if not matrix or not matrix[0]:
            return []
        m, n = len(matrix), len(matrix[0])
        ans = []
        helper(m, n, ans, matrix)
        return ans