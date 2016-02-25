class Solution:
    # @param nums: The integer array
    # @param target: Target number to find
    # @return the first position of target in nums, position start from 0 
    def binarySearch(self, nums, target):
        # write your code here
        
        # if not nums:
        #     return -1
        # length = len(nums)
        # left, right = 0, length - 1
        # while left < right:
        #     mid = left + (right - left) / 2
        #     if nums[mid] >= target:
        #         right = mid
        #     else:
        #         left = mid + 1
        # return right if nums[right] == target else -1
        if not nums:
            return -1
        else:
            length = len(nums)
            left, right = 0, length - 1
            while left + 1 < right:
                mid = left + (right - left) / 2
                if nums[mid] >= target:
                    right = mid
                else:
                    left = mid

            if nums[right] == target:
                return right
            elif nums[left] == target:
                return left
            else:
                return -1
            