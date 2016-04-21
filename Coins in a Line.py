class Solution:
    # @param n: an integer
    # @return: a boolean which equals to True if the first player will win
    def firstWillWin(self, n):
        # write your code here
        if n == 0:
            return False
        # dp = [False] * 4
        # dp[1 % 4] = True
        # dp[2 % 4] = True
        # dp[3 % 4] = False
        # dp[4 % 4] = True
        # if n > 4:
        #     # dp.extend([False] * (n + 1 - 5))
        #     for i in range(5, n + 1):
        #         dp[i % 4] = (dp[(i - 4) % 4] and dp[(i - 3) % 4]) or (dp[(i - 2) % 4] and dp[(i - 3) % 4])
        # return dp[n % 4]
        # return n % 3
        
        ## TLE: RuntimeError: maximum recursion depth exceeded
        def search(left, dp):
            if left == 0:
                return True
            if dp[left] != -2:
                return dp[left]
            if left == 1:
                dp[1] = True
            elif left == 2:
                dp[2] = True
            elif left == 3:
                dp[3] = False
            elif left == 4:
                dp[4] == True
            else:
                dp[left] = (search(left - 4, dp) and search(left - 3, dp)) or (search(left - 2, dp) and search(left - 3, dp))
            return dp[left]
            
        dp = [-2] * (n + 1)
        search(n, dp)
        return dp[n]
if __name__ == '__main__':
    print Solution().firstWillWin(9999)