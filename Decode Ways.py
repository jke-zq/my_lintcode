class Solution:
    # @param {string} s a string,  encoded message
    # @return {int} an integer, the number of ways decoding
    def numDecodings(self, s):
        # Write your code here
        if not s:
            return 0
        
        length = len(s)
        dp = [0] * (length + 1)
        dp[0] = 1
        dp[1] = int(s[0] != '0')
        for i in range(2, length + 1):
            if s[i - 1] != '0':
                dp[i] = dp[i - 1]
            val = int(s[i - 2:i])
            if 10 <= val <= 26:
                dp[i] += dp[i - 2]
        return dp[-1]