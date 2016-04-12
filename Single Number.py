class Solution:
    """
    @param A : an integer array
    @return : a integer
    """
    def singleNumber(self, A):
        # write your code here
        
        ans = 0
        for a in A:
            ans ^= a
        return ans