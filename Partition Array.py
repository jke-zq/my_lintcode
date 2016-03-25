class Solution:
    """
    @param nums: The integer array you should partition
    @param k: As description
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        # write your code here
        # you should partition the nums by k
        # and return the partition index as description
        if not nums:
            return 0
        
        length = len(nums)
        left, right = 0, length - 1
        pivot = 0
        while left <= right:
            if nums[left] < k:
                nums[pivot], nums[left] = nums[left], nums[pivot]
                pivot += 1
                left += 1
            else:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
        return pivot
            
