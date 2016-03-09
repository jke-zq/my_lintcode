class Solution: 
    # @param S, T: Two string.
    # @return: Count the number of distinct subsequences
    def numDistinct(self, S, T):
        # write your code here
        
        m, n = len(S), len(T)
        
        dp = [[0] * (n + 1) for __ in range(m + 1)]
        dp[0][0] = 1  # error
        for i in range(1, m + 1):
            dp[i][0] = 1 # error
                          # error
            for j in range(1, n + 1):
                dp[i][j] = dp[i - 1][j]
                if S[i - 1] == T[j - 1]:
                    dp[i][j] += dp[i - 1][j - 1]
        return dp[m][n]
                