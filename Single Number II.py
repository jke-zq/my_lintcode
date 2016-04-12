class Solution:
    """
	@param A : An integer array
	@return : An integer
    """
    def singleNumberII(self, A):
        # write your code here
        
        one, two = 0, 0
        for x in A:
            # one, two = (one & ~x) | (x & ~one & ~two), (two & ~x) | (x & one)
            oldOne = one
            one = (one & ~x) | (x & ~one & ~two)
            two = (two & ~x) | (x & oldOne)
        return one
        