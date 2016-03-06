class Solution:
    """
    @param grid: a list of lists of integers.
    @return: An integer, minimizes the sum of all numbers along its path
    """
    def minPathSum(self, grid):
        # write your code here
        
        m, n = len(grid), len(grid[0])
        ret = [[0] * (n) for __ in range(m)]
        ret[0][0] = grid[0][0]
        for i in range(1, n):
            ret[0][i] = grid[0][i] + ret[0][i - 1]
        for i in range(1, m):
            ret[i][0] = ret[i - 1][0] + grid[i][0]
            for j in range(1, n):
                ret[i][j] = min(ret[i][j - 1], ret[i - 1][j]) + grid[i][j]
        return ret[m - 1][n - 1]