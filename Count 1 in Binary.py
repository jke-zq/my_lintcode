class Solution:
    # @param num: an integer
    # @return: an integer, the number of ones in num
    def countOnes(self, num):
        # write your code here
        
        # ans = 0
        # while num:
        #     ans += 1
        #     num &= num - 1
        # return ans
        
        # ans = 0
        # while num:
        #     ans += num & 1
        #     num >>= 1
        # return ans
        
        ans = 0
        for __ in range(32):
            ans += num & 1
            num >>= 1
        return ans
        
####import:
## -1 is 0xFFFF...FFF(forever)
## all negative value should be right shift to -1