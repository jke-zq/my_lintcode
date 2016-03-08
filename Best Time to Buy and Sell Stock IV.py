class Solution:
    """
    @param k: an integer
    @param prices: a list of integer
    @return: an integer which is maximum profit
    """
    def maxProfit(self, k, prices):
        # write your code here
        
        ## judge null
        if not prices:
            return 0
        ## RE: MemoryError
        ## if k is bigger
        length = len(prices)
        if k >= length:
            local = prices[0]
            ret = 0
            for p in prices[1:]:
                if local < p:
                    ret += p - local
                    local = p
                else:
                    local = p
            return ret
        local = [0] * (k + 1)
        gl = [0] * (k + 1)
        # local = [[0] * (k + 1) for __ in range(length)]
        # gl = [[0] * (k + 1) for __ in range(length)]
        
        # gl[0][0] = 0
        # local[0][0] = 0
        # for i in range(1, k):
        #     local[0][i] = prices[0]
        #     gl[0][i] = prices[0]
        for i in range(1, length):
            # local[i][0] = 0
            # gl[i][0] = 0
            diff = prices[i] - prices[i - 1]
            for j in range(k, 0, -1):
                local[j] = max(gl[j - 1] + diff, local[j] + diff)
                gl[j] = max(gl[j], local[j])
                # local[i][j] = max(gl[i - 1][j - 1] + diff, local[i - 1][j] + diff)
                # gl[i][j] = max(gl[i - 1][j], local[i][j])
        return gl[k]
        # return gl[length - 1][k]

##solution two
class Solution:
    """
    @param k: an integer
    @param prices: a list of integer
    @return: an integer which is maximum profit
    """
    def maxProfit(self, k, prices):
        # write your code here
        if not prices:
            return 0
        
        length = len(prices)
        table = [[0] * (length + 1) for __ in range(length + 1)]
        
        table[0][0] = 0
        
        for i in range(length + 1):
            table[i][0] = 0
            for j in range(1, k + 1):
                sold = float('-inf')
                maxProfit = float('-inf')
                for s in range(i - 1, -1, -1):
                    if sold < prices[s]:
                        sold = prices[s]
                    else:
                        maxProfit = max(maxProfit, sold - prices[s])
                    table[i][j] = max(table[i][j], table[s][j - 1] + maxProfit)
        
        return table[length][k]