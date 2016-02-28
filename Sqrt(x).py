class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    """
    def sqrt(self, x):
        # write your code here
        
        left, right = 0, x
        while left + 1 < right:
            mid = left + (right - left) / 2
            if mid * mid <= x:
                left = mid
            else:
                right = mid
                
        #error: we should not check the left because there is no exception for the left.(0 is belong to the left * left <= x)
        # if left * left <= x:
        #     return left
        if right * right <= x:
            return right
        else:
            return left
                