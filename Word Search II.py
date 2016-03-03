class TrieNode:
    def __init__(self):
        self.isStr = False
        self.chars = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
    def add(self, word):
        p = self.root
        for w in word:
            if w not in p.chars:
                p.chars[w] = TrieNode()
            p = p.chars[w]
        p.isStr = True
        
class Solution:
    # @param board, a list of lists of 1 length string
    # @param words: A list of string
    # @return: A list of string
    def wordSearchII(self, board, words):
        # write your code here
        # def dfs(r, c, visited, ret, rows, cols, board, root, tmp):
        #     if root.isStr:
        #         ret.add(''.join(tmp))
        #     if 0 <= r < Rows and 0 <= c < Cols and not visited[r][c] and board[r][c] in root.chars:
        #         tmp.append(board[r][c])
        #         visited[r][c] = True
        #         nextroot = root.chars[board[r][c]]
        #         DICTS = ((-1, 0), (1, 0), (0, -1), (0, 1))
        #         for dx, dy in DICTS:
        #             nx, ny = r + dx, c + dy
        #             dfs(nx, ny, visited, ret, rows, cols, board, nextroot, tmp)
        #         tmp.pop()
        #         visited[r][c] = False
            
        # if not words or not board:
        #     return []
        # trie = Trie()
        # for word in words:
        #     trie.add(word)
        
        # Rows, Cols = len(board), len(board[0])
        # visited = [[False] * Cols for __ in range(Rows)]
        # ret = set()
        # tmp = []
        # for r in range(Rows):
        #     for c in range(Cols):
        #         dfs(r, c, visited, ret, Rows, Cols, board, trie.root, tmp)
        # return list(ret)
        def dfs(r, c, start, visited, tmp, ret, m, n, board, word):
            if start == len(word):
                ret.add(word)
                return
            if 0 <= r < m and 0 <= c < n and not visited[r][c] and word[start] == board[r][c]:
                tmp.append(board[r][c])
                visited[r][c] = True
                DICTS = ((-1, 0), (1, 0), (0, -1), (0, 1))
                for dx, dy in DICTS:
                    dfs(r + dx, c + dy, start + 1, visited, tmp, ret, m, n, board, word)
                tmp.pop()
                visited[r][c] = False
                
        m, n = len(board), len(board[0])
        visited = [[False] * n for __ in range(m)]
        tmp, ret = [], set()
        for word in words:
            for i in range(m):
                for j in range(n):
                    dfs(i, j, 0, visited, tmp, ret, m, n, board, word)
        return list(ret)
            
                