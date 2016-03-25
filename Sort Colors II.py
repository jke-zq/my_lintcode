class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sortColors2(self, colors, k):
        # write your code here
        
        def helper(start, end, kstart, kend, colors):
            if kstart >= kend or start >= end:
                return
            kmid = kstart + (kend - kstart) / 2
            left, pivot, right = start, start, end
            while left <= right:
                if colors[left] < kmid:
                    colors[pivot], colors[left] = colors[left], colors[pivot]
                    pivot += 1
                    left += 1
                elif colors[left] == kmid:
                    left += 1
                else:
                    colors[left], colors[right] = colors[right], colors[left]
                    right -= 1
            ##[pivot, left - 1] are all the kmid value
            helper(start, pivot - 1, kstart, kmid - 1, colors)
            helper(left, end, kmid + 1, kend, colors)
        
        if not colors:
            return None
        length = len(colors)
        helper(0, length - 1, 1, k, colors)