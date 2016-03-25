class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2 
    @return: nothing
    """
    def sortColors(self, nums):
        # write your code here
        
        if not nums:
            return None
        length = len(nums)
        left, pivot, right = 0, 0, length - 1
        while left <= right:
            if nums[left] == 0:
                nums[pivot], nums[left] = nums[left], nums[pivot]
                pivot += 1
                left += 1
            elif nums[left] == 1:
                left += 1
            else:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
        