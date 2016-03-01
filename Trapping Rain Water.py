class Solution:
    # @param heights: a list of integers
    # @return: a integer
    def trapRainWater(self, heights):
        # write your code here
        
        if not heights:
            return 0
            
        # tallestIndex, tallest = max(enumerate(heights), key = lambda x: x[1])
        # ret = 0
        # curTallest = 0
        # for hei in heights[:tallestIndex]:
        #     if curTallest < hei:
        #         curTallest = hei
        #     else:
        #         ret += curTallest - hei
        
        # curTallest = 0
        # for hei in heights[:tallestIndex:-1]:
        #     if curTallest < hei:
        #         curTallest = hei
        #     else:
        #         ret += curTallest - hei
        # return ret
        
        left, right = 0, len(heights) - 1
        ret = 0
        # leftHei, rightHei = heights[left], heights[right]
        leftHei, rightHei = 0, 0
        while left <= right:
            if leftHei < rightHei:
                if leftHei > heights[left]:
                    ret += leftHei - heights[left]
                else:
                    leftHei = heights[left]
                left += 1
            else:
                if rightHei > heights[right]:
                    ret += rightHei - heights[right]
                else:
                    rightHei = heights[right]
                right -= 1
        return ret
            
            
