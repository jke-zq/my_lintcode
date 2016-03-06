class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def climbStairs(self, n):
        # write your code here
        
        a, b = 0, 1
        for i in range(n):
            a, b = b, a + b
        return b
