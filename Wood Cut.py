class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    return: The maximum length of the small pieces.
    """
    def woodCut(self, L, k):
        # write your code here
        ##error
        if not L:
            return 0
        maxLen = max(L)
        left, right = 0, maxLen
        
        while left + 1 < right:
            mid = left + (right - left) / 2
            pices = reduce(lambda x, y: x + y / mid, L, 0)
            if pices >= k:
                left = mid
            ##error
            # elif pices == k:
            #     return mid
            else:
                right = mid

        pices = reduce(lambda x, y: x + y / right, L, 0)
        if pices >= k:
            return right
        
        # pices = reduce(lambda x, y: x + y / left, L, 0)
        # if pices >= k:
        #     return left
        return left

        