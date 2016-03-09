class Solution:
    """
    @params s1, s2, s3: Three strings as description.
    @return: return True if s3 is formed by the interleaving of
             s1 and s2 or False if not.
    @hint: you can use [[True] * m for i in range (n)] to allocate a n*m matrix.
    """
    def isInterleave(self, s1, s2, s3):
        # write your code here
        
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False
        dp = [[0] * (n + 1) for __ in range(m + 1)]
        dp[0][0] = 1
        for i in range(1, n + 1):
            if dp[0][i - 1] and s2[i - 1] == s3[i - 1]:
                dp[0][i] = dp[0][i - 1]
        print dp[0]
        for i in range(1, m + 1):
            if dp[i - 1][0] and s1[i - 1] == s3[i - 1]:
                dp[i][0] = dp[i - 1][0]
            for j in range(1, n + 1):
                if dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]:
                    dp[i][j] += dp[i - 1][j]
                    ## why break? Dont break!
                    # break
                if dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]:
                    dp[i][j] += dp[i][j - 1]
                    # break
            print dp[i]
        return dp[m][n]