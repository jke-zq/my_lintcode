class Solution:
    """
    @param A : An integer array
    @return : Two integer
    """
    def singleNumberIII(self, A):
        # write your code here
        x_xor_y = 0
        for a in A:
            x_xor_y ^= a
        ## x_xor_y = x ^ y
        # diffBit = x_xor_y & (~x_xor_y + 1)
        diffBit = x_xor_y & (-1 * x_xor_y)
        x, y = 0, 0
        for a in A:
            if a & diffBit:
                x ^= a
            else:
                y ^= a
        return x, y
        