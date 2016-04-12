class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        
        if not prices or len(prices) == 1:
            return 0
        i = float('inf')
        ret = float('-inf')
        for p in prices:
            if i > p:
                i = p
            else:
                ret = max(ret, p - i)
        return max(ret, 0)