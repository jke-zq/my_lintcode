class Solution:
    # @param {int[]} A an integer array
    # @return {int} an integer
    def stoneGame(self, A):
        # Write your code here
        
        def helper(start, end, length, dp, A):
            if start == end:
                dp[start][end] = 0
                return dp[start][end]
            if dp[start][end] != float('inf'):
                return dp[start][end]
            # total = sum(A[start:end + 1])
            # if start == end:
            #     dp[start][end] = total
            #     return dp[start][end]
            for i in range(start, end):
                dp[start][end] = min(dp[start][end],
                    helper(start, i, length, dp, A) + helper(i + 1, end, length, dp, A) + sums[end + 1] - sums[start])
            return dp[start][end]
            
        if not A:
            return 0
        length = len(A)
        sums = [0] * (length + 1)
        for i in range(length):
            sums[i + 1] = sums[i] + A[i]
        dp = [[float('inf')] * length for __ in range(length)]
        return helper(0, length - 1, length, dp, A)