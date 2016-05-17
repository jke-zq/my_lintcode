class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number 
             and the index of the last number
    """
    def subarraySum(self, nums):
        # write your code here
        
        if not nums:
            return []
        length = len(nums)
        ret = [0] * (length + 1)
        for i in range(length):
            ret[i + 1] = ret[i] + nums[i]
        
        dicts = {}
        for i in range(0, length + 1):
            # if ret[i] == 0:
            #     return [0, i - 1]
            # el
            if ret[i] in dicts:
                ## error [dicts[ret[i]] $- 1$, i - 1]
                return [dicts[ret[i]], i - 1]
            else:
                dicts[ret[i]] = i
        return []