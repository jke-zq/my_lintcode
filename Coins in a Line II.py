class Solution:
    # @param values: a list of integers
    # @return: a boolean which equals to True if the first player will win
    def firstWillWin(self, values):
        # write your code here
        
        length = len(values)
        if length < 3:
            return True
        dp = [0] * (length + 1)
        dp[length] = 0
        dp[length - 1] = values[-1]
        dp[length - 2] = values[-2] + values[-1]
        dp[length - 3] = values[length - 2] + values[length - 3]
        
        
        for i in range(length - 4, -1, -1):
            dp[i] = max(min(dp[i + 2], dp[i + 3]) + values[i], min(dp[i + 3], dp[i + 4]) + values[i] + values[i + 1])
        return dp[0] > sum(values) / 2
