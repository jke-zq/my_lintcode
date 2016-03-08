class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        
        if not prices or len(prices) == 1:
            return 0
        i = prices[0]
        ret = 0
        for p in prices[1:]:
            if i > p:
                i = p
            else:
                ret = max(ret, p - i)
        return ret