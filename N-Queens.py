class Solution:
    """
    Get all distinct N-Queen solutions
    @param n: The number of queens
    @return: All distinct solutions
    """
    def solveNQueens(self, n):
        # write your code here
        def helper(start, tmp, ret, n):
            if start == n:
                ret.append(printQueen(tmp))
                return
            # else:
            for i in range(n):
                if check(tmp, start, i):
                    tmp.append(i)
                    helper(start + 1, tmp, ret, n)
                    tmp.pop()
        
        def check(tmp, start, i):
            for r, c in enumerate(tmp):
                # diff = abs(i - c)
                # if c == i or diff == start - r:
                #     return False
                if c == i or r + c == start + i or r - c == start - i:
                    return False
            return True
        
        def printQueen(cols):
            length = len(cols)
            ret = [None] * length
            tmp = ['.'] * length
            for r, c in enumerate(cols):
                tmp[c] = 'Q'
                ret[r] = ''.join(tmp)
                tmp[c] = '.'
            return ret
        
        if n == 0:
            return []
        tmp, ret = [], []
        helper(0, tmp, ret, n)
        return ret
