class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be inserted
    @return : an integer
    """
    def searchInsert(self, A, target):
        # write your code here
        if not A:
            return 0
        
        left, right = 0, len(A) - 1
        while left + 1 < right:
            mid = left + (right - left) / 2
            # if A[mid] > target:
            if A[mid] >= target:
                right = mid
            elif A[mid] < target:
                left = mid
            else:
                return mid
        # if A[right] == target:
        #     return right
        # elif A[right] < target:
        #     return right + 1
        # if A[left] == target:
        #     return left
        # elif A[left] > target:
        #     return left
        # return left + 1
        if A[left] >= target:
            return left
        if A[right] < target:
            return len(A)
        else:
            return right