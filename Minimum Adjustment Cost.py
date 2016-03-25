class Solution:
    # @param A: An integer array.
    # @param target: An integer.
    def MinAdjustmentCost(self, A, target):
        # write your code here
        
        
        # dp[i][v] set the ith to v
        
        if not A:
            return 0 ## this is why dp[0] are all zero.
        length = len(A)
        dp = [[0] * (101) for __ in range(1 + length)]
        
        for i in range(1, length + 1):
            # dp[i][0] = float('inf')
            for v in range(1, 101):
                dp[i][v] = float('inf')
                for vv in range(1, 101):
                    if abs(v - vv) <= target:
                        dp[i][v] = min(dp[i][v], dp[i - 1][vv] + abs(A[i - 1] - v))
        
        return min(dp[length][1:])
        
        
                
