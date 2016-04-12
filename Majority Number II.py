class Solution:
    """
    @param nums: A list of integers
    @return: The majority number occurs more than 1/3
    """
    def majorityNumber(self, nums):
        # write your code here
        k = 3
        hashVal = collections.defaultdict(int)
        for n in nums:
            hashVal[n] += 1
            if len(hashVal) == k:
                for key in hashVal.keys():
                    hashVal[key] -= 1
                    if hashVal[key] == 0:
                        hashVal.pop(key)
        
        for key in hashVal.keys():
            hashVal[key] = 0
        
        for n in nums:
            if n in hashVal:
                hashVal[n] += 1
        
        length = len(nums)
        return [key for key in hashVal.keys() if hashVal[key] > length / k][0]