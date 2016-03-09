class Solution:
    """
    @param obstacleGrid: An list of lists of integers
    @return: An integer
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        # write your code here
        
        if not obstacleGrid or not obstacleGrid[0]:
           return 0
        
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        # dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        # dp = [0] * (n + 1)
        # for i in range(1, m + 1):
        #     dp[0] = 1 if i == 1 else 0
        #     for j in range(1, n + 1):
        #         if obstacleGrid[i - 1][j - 1] != 1:
        #             dp[j] = dp[j - 1] + dp[j]
        #         else:
        #             dp[j] = 0
        # return dp[n]
        dp = [0] * n
        dp[0] = 1 if obstacleGrid[0][0] == 0 else 0
        ## error
        for i in range(1, n):
            dp[i] = dp[i - 1] if obstacleGrid[0][i] == 0 else 0
        
        for i in range(1, m):
            ## error
            dp[0] = dp[0] if obstacleGrid[i][0] == 0 else 0
            for j in range(1, n):
                ## error: using dp[i]
                if obstacleGrid[i][j] == 0:
                    dp[j] += dp[j - 1]
                else:
                    dp[j] = 0
        return dp[n - 1]
