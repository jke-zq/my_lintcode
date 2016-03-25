class Solution:
    # @param values: a list of integers
    # @return: a boolean which equals to True if the first player will win
    def firstWillWin(self, values):
        # write your code here
        
        def memorySearch(start, end, dp, values):
            if start > end or 0 > start or start >= length or end < 0 or end >= length:
                return 0
            if dp[start][end] > 0:
                return dp[start][end]
            
            dp[start][end] = max(
                min(memorySearch(start + 2, end, dp, values), memorySearch(start + 1, end - 1, dp, values)) + values[start], 
                min(memorySearch(start, end - 2, dp, values), memorySearch(start + 1, end - 1, dp, values)) + values[end])
            return dp[start][end]
        
        length = len(values)
        dp = [[0] * length for __ in range(length)]
        return memorySearch(0, length - 1, dp, values) * 2 > sum(values)