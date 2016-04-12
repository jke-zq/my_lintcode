class Solution:
    """
    @param nums: a list of integers
    @return: A integer denote the sum of minimum subarray
    """
    def minSubArray(self, nums):
        # write your code here
        local = float('inf')
        gl = float('inf')
        for n in nums:
            local = min(local + n, n)
            gl = min(gl, local)
        
        return gl
