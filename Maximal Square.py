class Solution:
    #param matrix: a matrix of 0 and 1
    #return: an integer
    def maxSquare(self, matrix):
        # write your code here
        
        # dp[i][j] = min(dp[i - 1][j - ], up[i], lef) + 1 if matrix[i][j] == 1
        # up[i] = up[i - 1] + 1 if matrix[][i - 1] == 0 else 0
        # left[i] = left[i - 1] + 1 if
        if not matrix:
            return 
        length = len(matrix)
        n = len(matrix[0])
        up = [0] * n
        dp = [[0] * n for __ in range(2)]
        ans = 0
        for i in range(n):
            if matrix[0][i] == 1:
                dp[0][i] = 1 
                up[i] = 1
                ans = max(ans, dp[0][i])

        for i in range(1, length):
            left = 0
            # j == 0
            if matrix[i][0] == 1:
                dp[i % 2][0] = 1
                left = 1
                up[0] += 1
            else:
                up[0] = 0
            for j in range(1, n):
                if matrix[i][j] == 1:
                    dp[i % 2][j] = min(dp[(i - 1) % 2][j - 1], up[j], left) + 1
                    up[j] += 1
                    left += 1
                    ans = max(dp[i % 2][j], ans)
                else:
                    dp[i % 2][j] = 0
                    up[j] = 0
                    left = 0
        # m, n = len(matrix), len(matrix[0])
        # dp = [[0] * n for __ in range(2)]
        # ans = 0
        # for i in range(n):
        #     dp[0][i] = 1 if matrix[0][i] == 1 else 0
        #     ans = max(ans, dp[0][i])
        # for i in range(1, m):
        #     dp[i % 2][0] = 1 if matrix[i][0] == 1 else 0
        #     for j in range(1, n):
        #         if matrix[i][j] == 1:
        #             dp[i % 2][j] = min(dp[(i - 1) % 2][j - 1], dp[i % 2][j - 1], dp[(i - 1) % 2][j]) + 1
        #         else:
        #             dp[i % 2][j] = 0
        #     ans = max(ans, max(dp[i % 2]))
        return ans * ans
        