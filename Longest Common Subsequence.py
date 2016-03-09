class Solution:
    """
    @param A, B: Two strings.
    @return: The length of longest common subsequence of A and B.
    """
    def longestCommonSubsequence(self, A, B):
        # write your code here
        
        m, n = len(A), len(B)
        
        dp = [[0] * (n + 1) for __ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i][j])
        return dp[m][n]
