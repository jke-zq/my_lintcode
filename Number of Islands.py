class Solution:
    # @param {boolean[][]} grid a boolean 2D matrix
    # @return {int} an integer
    def numIslands(self, grid):
        # Write your code here
        
        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])
        count = 1
        queue = []
        dicts = ((-1, 0), (0, 1), (1, 0), (0, -1))
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    count += 1
                    grid[i][j] = count
                    queue.append((i, j))
                    while queue:
                        pos = queue.pop()
                        for r, c in dicts:
                            nr, nc = pos[0] + r, pos[1] + c
                            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                                grid[nr][nc] = count
                                queue.append((nr, nc))
        return count - 1