class Solution:
    """
    @param nums: A list of integers
    @return: The majority number
    """
    def majorityNumber(self, nums):
        # write your code here
        
        count = 1
        ans = float('inf')
        for n in nums:
            if n != ans:
                count -= 1
                if count == 0:
                    count = 1
                    ans = n
            else:
                count += 1
        return ans
