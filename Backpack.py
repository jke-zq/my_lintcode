class Solution:
    # @param m: An integer m denotes the size of a backpack
    # @param A: Given n items with size A[i]
    # @return: The maximum size
    def backPack(self, m, A):
        # write your code here
        
        
        dp = [0] * (m + 1)
        
        length = len(A)
        # for TLE
        if m > sum(A):
            return sum(A)
        for i in range(1, length + 1):
            for j in range(m, 0, -1):
                if j >= A[i - 1]:
                    dp[j] = max(dp[j], dp[j - A[i - 1]] + A[i - 1])
        return dp[m]
        
                