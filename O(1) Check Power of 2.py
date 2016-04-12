class Solution:
    """
    @param n: An integer
    @return: True or false
    """
    def checkPowerOf2(self, n):
        # write your code here
        
        if n != 0 and n & (n - 1) == 0:
            return True
        else:
            return False