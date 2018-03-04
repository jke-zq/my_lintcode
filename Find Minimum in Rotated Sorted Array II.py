class Solution:
    # @param num: a rotated sorted array
    # @return: the minimum number in the array
    def findMin(self, num):
        # write your code here

        # left, right = 0, len(num) - 1
        # while left + 1 < right:
        #     mid = left + (right - left) / 2
        #     while left + 1 < right and num[left] == num[right]:
        #         left += 1
        #     if num[mid] <= num[right]:
        #         right = mid
        #     else:
        #         left = mid

        # return min(num[left], num[right])


        left, right = 0, len(nums) - 1
        while left + 1 < right:
            # if nums[left] == nums[right]:
            #     right -= 1
            #     continue
            # mid = (left + right) // 2
            # if nums[mid] >= nums[left] and nums[left] > nums[right]:
            #     left = mid
            # else:
            #     right = mid
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid
            elif nums[mid] < nums[right]:
                right = mid
            else:
                right -= 1

        return min(nums[left], nums[right])
