class Solution:
    # @param {boolean[][]} grid a boolean 2D matrix
    # @return {int} an integer
    def numIslands(self, grid):
        # Write your code here
        
        # if not grid or not grid[0]:
        #     return 0
        
        # m, n = len(grid), len(grid[0])
        # count = 1
        # queue = []
        # dicts = ((-1, 0), (0, 1), (1, 0), (0, -1))
        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j] == 1:
        #             count += 1
        #             grid[i][j] = count
        #             queue.append((i, j))
        #             while queue:
        #                 pos = queue.pop()
        #                 for r, c in dicts:
        #                     nr, nc = pos[0] + r, pos[1] + c
        #                     if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
        #                         grid[nr][nc] = count
        #                         queue.append((nr, nc))
        # return count - 1
        
        ## uf
        # def compressed_find(x, fathers):
        #     parent = fathers[x]
        #     while parent != fathers[parent]:
        #         parent = fathers[parent]
            
        #     node = x
        #     while node != parent:
        #         tmp = fathers[node]
        #         fathers[node] = parent
        #         node = tmp
        #     return parent
        
        # def union(x, y, fathers):
        #     px, py = compressed_find(x, fathers), compressed_find(y, fathers)
        #     if px != py:
        #         fathers[px] = py
        
        # def do_union(i, j, rows, cols, fathers, grid, Dicts):
        #     x = transfer(i, j, cols)
        #     fathers[x] = x
        #     for dx, dy in Dicts:
        #         nx, ny = i + dx, j + dy
        #         if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
        #             y = transfer(nx, ny, cols)
        #             union(x, y, fathers)
                    
        # def transfer(i, j, cols):
        #     return i * cols + j - 1
        
        # if not grid or not grid[0]:
        #     return 0
        # rows, cols = len(grid), len(grid[0])
        # Dicts = ((-1, 0), (0, -1))
        # fathers = {}
        # for i in range(rows):
        #     for j in range(cols):
        #         if grid[i][j] == 1:
        #             do_union(i, j, rows, cols, fathers, grid, Dicts)
        # for key in fathers:
        #     compressed_find(key, fathers)
        # return len(set(fathers.values()))
        
        ## dfs
        def dfs(row, col, visited, ROWS, COLS, grid, DICTS):
            if row >= ROWS or row < 0 or col < 0 or col >= COLS:
                return
            if visited[row][col] or grid[row][col] == 0:
                return
            visited[row][col] = True
            for dx, dy in DICTS:
                nr, nc = row + dx, col + dy
                dfs(nr, nc, visited, ROWS, COLS, grid, DICTS)
            
        if not grid or not grid[0]:
            return 0
        ROWS, COLS = len(grid), len(grid[0])
        visited = [[False] * COLS for __ in range(ROWS)]
        DICTS = ((1, 0), (-1, 0), (0, 1), (0, -1))
        ans = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1 and not visited[i][j]:
                    dfs(i, j, visited, ROWS, COLS, grid, DICTS)
                    ans += 1
        return ans
                        