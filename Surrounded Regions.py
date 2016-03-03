class Solution:
    # @param {list[list[str]]} board a 2D board containing 'X' and 'O'
    # @return nothing 
    def surroundedRegions(self, board):
        # Write your code here
        
        if not board or not board[0]:
            return
        Rows, Cols = len(board), len(board[0])
        DICTS = ((-1, 0), (1, 0), (0, -1), (0, 1))
        for r in range(Rows):
            if r == 0 or r == Rows - 1:
                colums = range(Cols)
            else:
                colums = [0, Cols - 1]
            for c in colums:
                if board[r][c] == 'O':
                    queue = [(r, c)]
                    while queue:
                        ## error:using r, c = queue.pop(0) because the r the outside loop
                        cr, cc = queue.pop(0)
                        board[cr][cc] = '2'
                        for dx, dy in DICTS:
                            nr, nc = dx + cr, dy + cc
                            if 0 <= nr < Rows and 0 <= nc < Cols and board[nr][nc] == 'O':
                                queue.append((nr, nc))
        
        for r in range(Rows):
            for c in range(Cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                if board[r][c] == '2':
                    board[r][c] = 'O'