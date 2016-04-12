class Solution:
    # @param n a integer
    # @return ans a integer
    def trailingZeros(self, n):
        
        factor = 5
        ans = 0
        while n / factor > 0:
            ans += n / factor
            factor *= 5
        return ans
        