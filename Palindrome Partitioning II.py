class Solution:
    # @param s, a string
    # @return an integer
    def minCut(self, s):
        # write your code here
        def palindrome(s):
            if not s:
                return
            #dp[i][j] = dp[i + 1][j - 1] and s[i] == s[j]
            length = len(s)
            dp = [[False] * length for __ in range(length)]
            ## error k:0 - length - 1
            for k in range(0, length):
                i = 0
                while i + k < length:
                    if s[i] == s[i + k]:
                        if k >= 2:
                            dp[i][i + k] = dp[i + 1][i + k - 1]
                        else:
                            dp[i][i + k] = True
                    i += 1
            return dp
                        
        def check(left, right, s):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
            
        length = len(s)
        ans = [float('inf')] * (length + 1)
        ans[0] = -1 # 'aaaa' result is 0, ans[0] + 'aaaa' = 0, so ans[0] = -1
        isPalindromes = palindrome(s)
        # print isPalindromes
        for i in range(1, length + 1):
            for j in range(0, i):
                ## TLE: using dp to get dp[i][j] to shwo if s[i]-s[j] is palindrome
                if ans[j] != float('inf') and isPalindromes[j][i - 1]:
                    ans[i] = min(ans[i], ans[j] + 1)
        
        return ans[length]
        