class Solution:
    # @param {int[]} A an integer array
    # @param {int[]} V an integer array
    # @param {int} m an integer
    # @return {int} an array
    def backPackIII(self, A, V, m):
        # Write your code here
        
        if not A or not V or m == 0:
            return 0
        ## transfer into the backpack II
        # NA, NV = [], []
        # for index, v in enumerate(A):
        #     times = m / v
        #     for __ in range(times):
        #         NA.append(A[index])
        #         NV.append(V[index])
        
        ## backpack II; TLE
        # NA, NV = A, V
        # length = len(NA)
        # dp = [[0] * (m + 1) for __ in range(2)]
        
        # for i in range(1, length + 1):
        #     for j in range(1, m + 1):
        #         dp[i % 2][j] = dp[(i - 1) % 2][j]
        #         times = j / NA[i - 1]
        #         for t in range(1, times + 1):
        #             # if j >= NA[i - 1]:
        #             dp[i % 2][j] = max(dp[i % 2][j], dp[(i - t) % 2][j - t * NA[i - 1]] + t * NV[i - 1])
        # return dp[length % 2][m]
        
        ## there is no restriction to [index][*], only [m].
        dp = [0] * (m + 1)
        for a, v in zip(A, V):
            for  j in range(a, m + 1):
                dp[j] = max(dp[j], dp[j - a] + v)
        return dp[m]