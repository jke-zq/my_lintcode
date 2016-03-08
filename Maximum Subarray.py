class Solution:
    """
    @param nums: A list of integers
    @return: An integer denote the sum of maximum subarray
    """
    def maxSubArray(self, nums):
        # write your code here
        
        local = nums[0]
        gl = nums[0]
        for n in nums[1:]:
            local = max(local + n, n)
            gl = max(gl, local)
        return gl