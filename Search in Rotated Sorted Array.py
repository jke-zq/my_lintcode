class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : an integer
    """
    def search(self, A, target):
        # write your code here
        
        if not A:
            return -1
        left, right = 0, len(A) - 1
        while left + 1 < right:
            mid = left + (right - left) / 2
            if A[mid] == target:
                return mid            
            elif target >= A[left]:
                if target > A[mid] > A[left]:
                    left = mid
                else:
                    right = mid
            elif target <= A[right]:
                if A[right] > A[mid] > target:
                    right = mid
                else:
                    left = mid
        
        if A[left] == target:
            return left
        if A[right] == target:
            return right
        return -1