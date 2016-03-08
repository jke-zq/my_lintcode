class Solution:
    # @param nums: an integer[]
    # @return: an integer
    def maxProduct(self, nums):
        # write your code here
        localMin, localMax = nums[0], nums[0]
        gl = localMax
        for n in nums[1:]:
            # localMin, localMax = min(localMin * n, localMax * n, n), max(localMax * n, localMin * n, n)
            l1, l2 = localMin * n, localMax * n
            localMin = min(l1, l2, n)
            localMax = max(l1, l2, n)
            gl = max(localMax, gl)
        return gl