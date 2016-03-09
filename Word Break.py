class Solution:
    # @param s: A string s
    # @param dict: A dictionary of words dict
    def wordBreak(self, s, dict):
        # write your code here
        ## handle s = '' and dict = [], 
        ## len(s) == 0 when s == ''
        length = len(s)
        dp = [False] * (length + 1)
        dp[0] = True
        sets = set(dict)
        for i in range(1, length + 1):
            for j in range(i - 1, -1, -1):
                if dp[j] and s[j:i] in sets:
                    dp[i] = True
                    break
        return dp[length]

                
