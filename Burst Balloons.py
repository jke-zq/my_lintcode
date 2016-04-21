class Solution(object):
    """
    @param {int[]} nums a list of integer
    @return {int} an integer, maximum coins
    """
    def maxCoins(self, nums):
        # Write your code here
        
        def search(left, right, dp, nums):
            ## to get init value of the least state, just use the second least state
            ## 1 5 1 == 0 + 1 * 5 * 1 + 0, so search(0, 1) = 0
            if left + 1 >= right:
                return 0
            if dp[left][right] != -1:
                return dp[left][right]
            for x in range(left + 1, right):
                dp[left][right] = max(dp[left][right], search(left, x, dp, nums) +  nums[x] * nums[left] * nums[right] + search(x, right, dp, nums))
            return dp[left][right]
            
        if not nums:
            return 0
        
        nums.insert(0, 1)
        nums.append(1)
        length = len(nums)
        dp = [[-1] * length for __ in range(length)]
        return search(0, length - 1, dp, nums)