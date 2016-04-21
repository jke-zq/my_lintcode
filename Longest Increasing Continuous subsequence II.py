import operator
class Solution:
    # @param {int[][]} A an integer matrix
    # @return {int}  an integer
    def longestIncreasingContinuousSubsequenceII(self, A):
        # Write your code here        
        # def search(r, c, visited, ans, A, rows, cols, op):
        #     if r < 0 or c < 0 or r >= rows or c >= cols:
        #         return 0
            
        #     if visited[r][c] != -1:
        #         return visited[r][c]
            
        #     count = 1
        #     if c > 0:
        #         ret = search(r, c - 1, visited, ans, A, rows, cols, op)
        #         if op(A[r][c], A[r][c - 1]):
        #             count = max(count, 1 + ret)
        #     if c < cols - 1:
        #         ret = search(r, c + 1, visited, ans, A, rows, cols, op)
        #         if op(A[r][c], A[r][c + 1]):
        #             count = max(count, 1 + ret)
        #     if r > 0:
        #         ret = search(r - 1, c, visited, ans, A, rows, cols, op)
        #         if op(A[r][c], A[r - 1][c]):
        #             count = max(count, 1 + ret)
        #     # if r < rows - 1:
        #     #     ret = search(r + 1, c, visited, ans, A, rows, cols, op)
        #     #     if op(A[r][c], A[r + 1][c]):
        #     #         count = max(count, 1 + ret)
        #     visited[r][c] = count
        #     ans[0] = max(visited[r][c], ans[0])
        #     return visited[r][c]
            
        # if not A or not A[0]:
        #     return 0
        
        # rows = len(A)
        # cols = len(A[0])
        # ans = [0]
        # inc = [[-1] * cols for __ in range(rows)]
        # dec = [[-1] * cols for __ in range(rows)]
        # search(rows - 1, cols - 1, inc, ans, A, rows, cols, operator.gt)
        # search(rows - 1, cols - 1, dec, ans, A, rows, cols, operator.lt)
        # return ans[0]
        
        ## solution two
        ## solution two
        DICTS = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        def search(i, j, flag, dp, A, rows, cols):
            if flag[i][j] != 0:
                return dp[i][j]
            ans = 1
            for dx, dy in DICTS:
                nx, ny = i + dx, j + dy
                # if nx >= 0 and nx < rows and ny >= 0 and ny < cols and A[i][j] > A[nx][ny]:
                if nx >= 0 and nx < rows and ny >= 0 and ny < cols and A[i][j] < A[nx][ny]:
                    ans = max(ans, 1 + search(nx, ny, flag, dp, A, rows, cols))
            flag[i][j] = 1
            dp[i][j] = ans
            return ans
         
        if not A:
            return 0
        rows = len(A)
        cols = len(A[0])
        flag = [[0] * cols for __ in range(rows)]
        dp = [[0] * cols for __ in range(rows)]
        ans = 1
        for i in range(rows):
            for j in range(cols):
                search(i, j, flag, dp, A, rows, cols)
                ans = max(ans, dp[i][j])
        print ans
        return ans


if __name__ == '__main__':
    A = [
  [1 ,2 ,3 ,4 ,5],
  [16,17,24,23,6],
  [15,18,25,22,7],
  [14,19,20,21,8],
  [13,12,11,10,9]
]
    Solution().longestIncreasingContinuousSubsequenceII(A)
        
