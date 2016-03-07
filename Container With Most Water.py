class Solution:
    # @param heights: a list of integers
    # @return: an integer
    def maxArea(self, heights):
        # write your code here
        if not heights:
            return 0
        
        length = len(heights)
        left, right = 0, length - 1
        ret = 0
        while left < right:
            if heights[left] > heights[right]:
                ret = max(ret, heights[right] * (right - left))
                right -= 1
            else:
                ret = max(ret, heights[left] * (right - left))
                left += 1
        return ret

        