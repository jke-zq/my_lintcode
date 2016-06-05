class Solution:
    """
    @param a: The first integer
    @param b: The second integer
    @return:  The sum of a and b
    """
    def aplusb(self, a, b):
        
        MAX_BIT = 2**32
        MAX_BIT_COMPLIMENT = -2**32
        while b:
            if b == MAX_BIT:
                return a ^ MAX_BIT_COMPLIMENT
            carry = a & b
            a = a ^ b
            b = carry << 1
    
        return a