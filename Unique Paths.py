class Solution:
    """
    @param n and m: positive integer(1 <= n , m <= 100)
    @return an integer
    """ 
    def uniquePaths(self, m, n):
        # write your code here
        
        ret = [[0] * n for __ in range(m)]
        for i in range(n):
            ret[0][i] = 1
        for i in range(1, m):
            ret[i][0] = ret[i - 1][0]
            for j in range(1, n):
                ret[i][j] = ret[i - 1][j] + ret[i][j - 1]
        return ret[m - 1][n - 1]