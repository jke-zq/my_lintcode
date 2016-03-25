class Solution:
    # @param n: an integer
    # @return: a boolean which equals to True if the first player will win
    def firstWillWin(self, n):
        # write your code here
        if n == 0:
            return False
        dp = [False] * 4
        dp[1 % 4] = True
        dp[2 % 4] = True
        dp[3 % 4] = False
        dp[4 % 4] = True
        if n > 4:
            # dp.extend([False] * (n + 1 - 5))
            for i in range(5, n + 1):
                dp[i % 4] = (dp[(i - 4) % 4] and dp[(i - 3) % 4]) or (dp[(i - 2) % 4] and dp[(i - 3) % 4])
        return dp[n % 4]
                