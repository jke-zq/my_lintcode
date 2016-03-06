class Solution:
    """
    @param nums: The integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence(self, nums):
        # write your code here
        if not nums:
            return 0
        
        length = len(nums)
        ret = [1] * length
        for i in range(1, length):
            for j in range(i - 1, -1, -1):
                if nums[i] >= nums[j]:
                    ret[i] = max(ret[i], 1 + ret[j])
                    # error: all smaller one
                    # ret[i] = ret[i] + ret[j]
                    # break
        return max(ret)
