class Solution:
    # @param {int[]} A an integer array
    # @return {int} an integer
    def stoneGame2(self, A):
        # Write your code here
        n = len(A)
        if n <= 1:
            return 0

        s = [0]
        dp = [[sys.maxint for i in xrange(2 * n)] for j in xrange(2 * n)]
        for i in xrange(2 * n):
            s.append(s[-1] + A[i % n])
            dp[i][i] = 0

        for l in xrange(2, 2 * n + 1):
            for i in xrange(2 * n):
                j = i + l - 1
                if j >= 2 * n:
                    continue
                for k in xrange(i, j):
                    dp[i][j] = min(dp[i][k] + dp[k+1][j] + s[j + 1] - s[i], dp[i][j])

        ans = sys.maxint
        for i in xrange(n):
            ans = min(ans, dp[i][i + n - 1])
        return ans
