class Solution:
    # @param {boolean[][]} matrix, a list of lists of boolean
    # @return {int} an integer
    def maximal_rectangle(self, matrix):
        # Write your code here
        if not matrix:
            return 0

        m, n = len(matrix), len(matrix[0])
        up = [0] * (n + 1)
        # MLE
        # dp = [[(0, 0)] * (n + 1) for __ in range(m + 1)]
        dp = [[(0, 0)] * (n + 1) for __ in range(3)]
        # init the first row and the first col
        ans = 0
        for i in range(1, m + 1):
            left = 0
            for j in range(1, n + 1):
                if matrix[i - 1][j - 1]:
                    left += 1
                    up[j] += 1
                    # if dp[(i - 1) % 3][j - 1] == (0, 0):
                    if left > up[j]:
                        dp[i % 3][j] = (left, 1)
                    else:
                        dp[i % 3][j] = (1, up[j])
                    rleft = (dp[i % 3][j - 1][0] + 1, min(dp[i % 3][j - 1][1], up[j]))
                    rmid = (min(1 + dp[(i - 1) % 3][j - 1][0], left), min(1 + dp[(i - 1) % 3][j - 1][1], up[j]))
                    rright = (min(left, dp[(i - 1) % 3][j][0]), dp[(i - 1) % 3][j][1] + 1)
                    ans_, ans_tuple = max((rleft[0] * rleft[1], rleft), (rmid[0] * rmid[1], rmid), (rright[0] * rright[1], rright))
                    if max(dp[i % 3][j]) > ans_:
                        ans_ = max(dp[i % 3][j])
                    else:
                        dp[i % 3][j] = ans_tuple
                    ans = max(ans, ans_)
                else:
                    left = 0
                    up[j] = 0
                    dp[i % 3][j] = (0, 0)
        return ans
