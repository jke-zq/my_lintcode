class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        # write your code here
        def dfs(row, col, pos, visited, rows, cols, length, board, word, DICTS):
            if row < 0 or row >= rows or col < 0 or col >= cols or visited[row][col]:
                return False
            if board[row][col] != word[pos]:
                return False
            pos += 1
            if pos == length:
                return True
            visited[row][col] = True
            for x, y in DICTS:
                nx, ny = row + x, col + y
                if dfs(nx, ny, pos, visited, rows, cols, length, board, word, DICTS):
                    return True
            visited[row][col] = False
            return False
            
        
        if not board or not board[0]:
            return False
        rows, cols = len(board), len(board[0])
        length = len(word)
        DICTS = ((-1, 0), (1, 0), (0, -1), (0, 1))
        visited = [[False] * cols for __ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0, visited, rows, cols, length, board, word, DICTS):
                    return True
        return False
            