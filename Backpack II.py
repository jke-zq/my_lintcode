class Solution:
    # @param m: An integer m denotes the size of a backpack
    # @param A & V: Given n items with size A[i] and value V[i]
    # @return: The maximum value
    def backPackII(self, m, A, V):
        # write your code here
        
        length = len(A)
        dp = [[0] * (m + 1) for __ in range(2)]
        
        for i in range(1, length + 1):
            for j in range(1, m + 1):
                dp[i % 2][j] = dp[(i - 1) % 2][j]
                if A[i - 1] <= j:
                    dp[i % 2][j] = max(dp[i % 2][j], dp[(i - 1) % 2][j - A[i - 1]] + V[i - 1])
        return dp[length % 2][m]