class Solution:
    # @param values: a list of integers
    # @return: a boolean which equals to True if the first player will win
    def firstWillWin(self, values):
        # write your code here
        
        # length = len(values)
        # if length < 3:
        #     return True
        # dp = [0] * (length + 1)
        # dp[length] = 0
        # dp[length - 1] = values[-1]
        # dp[length - 2] = values[-2] + values[-1]
        # dp[length - 3] = values[length - 2] + values[length - 3]
        
        
        # for i in range(length - 4, -1, -1):
        #     dp[i] = max(min(dp[i + 2], dp[i + 3]) + values[i], min(dp[i + 3], dp[i + 4]) + values[i] + values[i + 1])
        # # return dp[0] > sum(values) / 2
        # return 2 * dp[0] > sum(values)
        
        ## this is wrong order.
        # length = len(values)
        # if length < 3:
        #     return True
        # dp = [0] * (length + 1)
        # # values = values[::-1]
        # dp[0] = 0 ## zero coins
        # dp[1] = values[0]
        # dp[2] = values[0] + values[1]
        # dp[3] = values[0] + values[1]
        
        # for i in range(4, length + 1):
        #     dp[i] = max(min(dp[i - 2], dp[i - 3]) + values[i - 1], min(dp[i - 3], dp[i - 4]) + values[i - 1] + values[i - 2])
        
        # return 2 * dp[length] > sum(values)
        
        ## search + mem
        def search(left, dp, values, length):
            if left < 0:
                return 0
            if dp[left] > 0:
                return dp[left]
            if left == 0:
                dp[0] = 0
            elif left == 1:
                dp[1] = values[length - 1]
            elif left == 2:
                dp[2] = values[-1] + values[-2]
            elif left == 3:
                dp[3] = values[-2] + values[-3]
            else:
                dp[left] = max(min(search(left - 2, dp, values, length), search(left - 3, dp, values, length)) + values[length - left], min(search(left - 3, dp, values, length), search(left - 4, dp, values, length)) + values[length - left] + values[length - left + 1])
            return dp[left]
            
        if not values:
            return 0
        length = len(values)
        dp = [0] * (length + 1)
        search(length, dp, values, length)
        return dp[length] * 2 > sum(values)