class Solution:
    """
    @param nums: A list of integers
    @param k: As described
    @return: The majority number
    """
    def majorityNumber(self, nums, k):
        # write your code here
        
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


## ugly
#### using for k in hashV.keys(): and k in arguments will be reseted 
class Solution:
    """
    @param nums: A list of integers
    @param k: As described
    @return: The majority number
    """
    def majorityNumber(self, nums, k):
        # write your code here
        hashV = collections.defaultdict(int)
        for n in nums:
            hashV[n] += 1
            if len(hashV) == k:
                for key in hashV.keys():
                    hashV[key] -= 1
                    if hashV[key] == 0:
                        hashV.pop(key)
                        # break
        # print hashV
        hashV = hashV.fromkeys(hashV.keys(), 0)
        # print hashV
        for n in nums:
            if n in hashV:
                hashV[n] += 1
        # print hashV
        length = len(nums)
        return [key for key in hashV.keys() if hashV[key] * 1.0 / length > 1.0 / k][0]
