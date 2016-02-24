class Solution:
    # @param nums, an array of integer
    # @param target, an integer
    # @return an integer
    def twoSum2(self, nums, target):
        # Write your code here
        nums.sort()
        i, j = 0, len(nums) - 1
        ret = 0
        while i < j:
            if nums[i] + nums[j] > target:
                ret += j - i
                j -= 1
            else:
                i += 1
        return ret