class Solution:
    """
    @param nums: A list of integers
    @return: An integer denotes the sum of max two non-overlapping subarrays
    """
    def maxTwoSubArrays(self, nums):
        # write your code here
        if not nums:
            return 0
        length = len(nums)
        leftMax = [0] * length
        local = float('-inf')
        gl = float('-inf')
        for i in range(length):
            local = max(local + nums[i], nums[i])
            gl = max(local, gl)
            leftMax[i] = gl
        
        rightMax = [0] * length
        local = float('-inf')
        gl = float('-inf')
        for i in range(length - 1, -1, -1):
            local = max(local + nums[i], nums[i])
            gl = max(gl, local)
            rightMax[i] = gl
        
        ans = float('-inf')
        for i in range(length - 1):
            ans = max(ans, leftMax[i] + rightMax[i + 1])
        return ans
