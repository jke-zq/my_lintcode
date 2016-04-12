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
        ret = 0
        for p in prices:
            if i < p:
                ret += p - i
                ## after sold, reset i with p
                i = p
            else:
                i = p
        return max(ret, 0)


maximum sum subarray:
不带区间                第i个元素并入上一个local[i-1]            不能并入,开始重新累加
local[i]        = max("local[i - 1] + nums[i]",             ###nums[i])
best time to buy stock:
有‘区间’               第i个元素并入上一个local[i-1](的最后区间)   不能并入,开始新开辟一个’区间‘
local[i][j - 1] = max("local[i - 1][j] + op(nums[i]",        ###nums[i - 1] + op(nums[i]) + (0 - (i - 1) 中j - 1的全局最优))
