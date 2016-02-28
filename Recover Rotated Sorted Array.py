class Solution:
    """
    @param nums: The rotated sorted array
    @return: nothing
    """
    def recoverRotatedSortedArray(self, nums):
        # write your code here
        
        i = 0
        length = len(nums)
        while i < length - 1:
            if nums[i] <= nums[i + 1]:
                i += 1
            else:
                break
        if i == length - 1:
            return
        else:
            ##error
            # nums[0:i + 1] = nums[0:i + 1:-1]
            # nums[i + 1:length] = nums[i + 1:length:-1]
            # nums[:] = nums[::-1]
            ##a = reversed(a)
            #   #>>> r[1:1]=[9,8]
                # >>> r
                # [1, 9, 8, 2, 3, 4]
                # >>> r[1:1]=['blah']
                #>>> r
                # [1, 'blah', 9, 8, 2, 3, 4]
            nums[:i + 1] = nums[i::-1]
            nums[i + 1:] = nums[:i:-1]
            # nums[i + 1:] = nums[length - 1:i:-1]
            ##alse used: nums.reverse()
            nums[:] = nums[::-1]
            ##All slice operations return a new list containing the requested elements.
            print nums


if __name__ == '__main__':
    nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    # nums = [3,4,0,1,2]
    Solution().recoverRotatedSortedArray(nums)