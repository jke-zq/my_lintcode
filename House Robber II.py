class Solution:
    # @param nums: A list of non-negative integers.
    # return: an integer
    def houseRobber2(self, nums):
        # write your code here
        def houseRobber(nums):
            length = len(nums)
            if length == 1:
                return nums[0]
            elif length == 2:
                return max(nums[0], nums[1])
            dp = [0] * 3
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            for i in range(2, length):
                dp[i % 3] = max(dp[(i - 1) % 3], dp[(i - 2) % 3] + nums[i])
            return dp[(length - 1) % 3]

        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        ans1 = houseRobber(nums[1:])
        # nums.append(nums.pop(0))
        ans2 = houseRobber(nums[:-1])
        return max(ans1, ans2)
