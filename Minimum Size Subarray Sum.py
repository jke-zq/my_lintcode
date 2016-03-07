class Solution:
     # @param nums: a list of integers
     # @param s: an integer
     # @return: an integer representing the minimum size of subarray
    def minimumSize(self, nums, s):
        # write your code here
        ## TLE
        # if not nums:
        #     return -1
        # length = len(nums)
        # ret = float('inf')
        # for i in range(length):
        #     total = 0
        #     j = i
        #     while j < length:
        #         total += nums[j]
        #         if total < s:
        #             j += 1
        #         else:
        #             ret = min(ret, j - i + 1)
        #             break
        # return -1 if ret == float('inf') else ret