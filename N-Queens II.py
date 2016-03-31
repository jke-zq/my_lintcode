class Solution:
    """
    Calculate the total number of distinct N-Queen solutions.
    @param n: The number of queens.
    @return: The total number of distinct solutions.
    """
    def totalNQueens(self, n):
        # write your code here
        def helper(start, positions, ret, n):
            if start == n:
                ret[0] += 1
                return
            for i in range(n):
                if check(start, i, positions):
                    positions.append(i)
                    helper(start + 1, positions, ret, n)
                    positions.pop()
        
        def check(rw, cl, positions):
            for r, c in enumerate(positions):
                if cl == c or r + c == cl + rw or r - c == rw - cl:
                    return False
            return True
        
        positions, ret = [], [0]
        helper(0, positions, ret, n)
        return ret[0]
        
        
        
        
        
        
        
        
