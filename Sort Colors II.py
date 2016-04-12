class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sortColors2(self, colors, k):
        # write your code here
        
        # def helper(start, end, kstart, kend, colors):
        #     if kstart >= kend or start >= end:
        #         return
        #     kmid = kstart + (kend - kstart) / 2
        #     left, pivot, right = start, start, end
        #     while left <= right:
        #         if colors[left] < kmid:
        #             colors[pivot], colors[left] = colors[left], colors[pivot]
        #             pivot += 1
        #             left += 1
        #         elif colors[left] == kmid:
        #             left += 1
        #         else:
        #             colors[left], colors[right] = colors[right], colors[left]
        #             right -= 1
        #     ##[pivot, left - 1] are all the kmid value
        #     helper(start, pivot - 1, kstart, kmid - 1, colors)
        #     helper(left, end, kmid + 1, kend, colors)
        
        # if not colors:
        #     return None
        # length = len(colors)
        # helper(0, length - 1, 1, k, colors)
        
        length = len(colors)
        for i in range(length):
            if colors[i] > 0:
                while colors[colors[i] - 1] > 0 and colors[i] != i + 1 and colors[i] != colors[colors[i] - 1]:
                    colors[colors[i] - 1], colors[i] = -1, colors[colors[i] - 1]
                if colors[i] == i + 1:
                    colors[i] = -1
                elif colors[i] == colors[colors[i] - 1]:
                    colors[colors[i] - 1] = -2
                    colors[i] = 0
                else:
                    colors[colors[i] - 1] -= 1
                    colors[i] = 0
        
        index = length - 1
        while k > 0:
            pos = colors[k - 1] + index + 1
            while index >= pos:
                colors[index] = k
                index -= 1
            k -= 1