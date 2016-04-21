class Solution:
    # @param nums: a list of integers
    # @return: nothing
    def partitionArray(self, nums):
        # write your code here
        
        if not nums:
            return
        length = len(nums)
        left, right = 0, length - 1
        pivot = 0
        while left <= right:
            if nums[left] % 2 == 1:
                nums[pivot], nums[left] = nums[left], nums[pivot]
                pivot += 1
                left += 1
            else:
                left += 1
        
