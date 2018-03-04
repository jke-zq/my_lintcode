class Solution:
    """
    @param: nums: an array with positive and negative numbers
    @param: k: an integer
    @return: the maximum average
    """
    def maxAverage(self, nums, k):
        # write your code here

        start, end = min(nums), max(nums)
        n = len(nums)
        prefix = [0] * (n + 1)
        while end - start > 1e-6:
            mid, check = (start + end) / 2, False
            mid_pre = 0
            for i in range(1, n + 1):
                prefix[i] = prefix[i - 1] + nums[i - 1] - mid
                if i >= k and prefix[i] >= mid_pre:
                    check = True
                    break
                if i >= k:
                    mid_pre = min(mid_pre, prefix[i - k + 1])
            if check:
                start = mid
            else:
                end = mid

        return start

