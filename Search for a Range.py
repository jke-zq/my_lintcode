class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : a list of length 2, [index1, index2]
    """
    def searchRange(self, A, target):
        # write your code here
        if not A:
            return [-1, -1]
            
        ret = [-1, -1]
        left, right = 0, len(A) - 1
        while left + 1 < right:
            mid = left + (right - left) / 2
            if A[mid] >= target:
                right = mid
            else:
                left = mid
                
        if A[left] == target:
            ret[0] = left
        elif A[right] == target:
            ret[0] = right

        
        left, right = 0, len(A) - 1
        while left + 1 < right:
            mid = left + (right - left) / 2
            if A[mid] > target:
                right = mid
            else:
                left = mid
                
        if A[left] == target:
            ret[1] = left
        if A[right] == target:
            ret[1] = right
        return ret
        