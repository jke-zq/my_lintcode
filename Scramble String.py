class Solution:
    # @param {string} s1 A string
    # @param {string} s2 Another string
    # @return {boolean} whether s2 is a scrambled string of s1
    def isScramble(self, s1, s2):
        # Write your code here
        
        def memorySearch(start1, start2, length, dp, s1, s2):
            if length == 1:
                dp[start1][start2][length] = s1[start1] == s2[start2]
                return dp[start1][start2][length]
            if dp[start1][start2][length] is not None:
                return dp[start1][start2][length]
            
            for i in range(1, length):
                dp[start1][start2][length] = (
                    (memorySearch(start1, start2, i, dp, s1, s2) and 
                     memorySearch(start1 + i, start2 + i, length - i, dp, s1, s2))
                    or 
                    (memorySearch(start1, start2 + length - i, i, dp, s1, s2) and 
                     memorySearch(start1 + i, start2, length - i, dp, s1, s2))
                    )
                if dp[start1][start2][length]:
                    break
            return dp[start1][start2][length]
        
        
        
        
        if not s1:
            return False
            
        length = len(s1)
        if len(s2) != length:
            return False
        
        dp = [[[None] * (length + 1) for __ in range(length)] for __ in range(length)]
        return memorySearch(0, 0, length, dp, s1, s2)