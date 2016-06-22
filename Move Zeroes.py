class Solution:
    # @param {int[]} nums an integer array
    # @return nothing, do this in-place
    def moveZeroes(self, nums):
        # Write your code here
        
        if not nums:
            return
        length = len(nums)
        pre = 0
        for i in range(length):
            if nums[i] != 0:
                nums[pre], nums[i] = nums[i], nums[pre]
                pre += 1