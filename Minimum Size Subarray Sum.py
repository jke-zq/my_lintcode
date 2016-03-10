class Solution:
     # @param nums: a list of integers
     # @param s: an integer
     # @return: an integer representing the minimum size of subarray
    def minimumSize(self, nums, s):
        # write your code here
        if not nums:
            return -1
        length = len(nums)
        ret = float('inf')
        total = 0
        j = 0
        for i in range(length):
            total += nums[i]
            # while total >= s:
            #     ret = min(ret, i - j + 1)
            #     total -= nums[j]
            #     j += 1
            ## templet
            while j <= i:
                if total >= s:
                    ret = min(ret, i - j + 1)
                    total -= nums[j]
                    j += 1
                else:
                    break
            
        return -1 if ret == float('inf') else ret