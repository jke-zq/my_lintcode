class Solution:
    """
    @param A : an integer ratated sorted array and duplicates are allowed
    @param target : an integer to be searched
    @return : a boolean
    """
    def search(self, A, target):
        # write your code here
        
        if not A:
            return False
        left, right = 0, len(A) - 1
        while left + 1 < right:
            
            while left + 1 < right and A[left] == A[right]:
                left += 1
            mid = left + (right - left) / 2
            if A[mid] == target:
                return True

            # if target >= A[left]:
            #     if A[left] <= A[mid] < target:
            #         left = mid
            #     else:
            #         right = mid
            # else:
            #     if A[right] >= A[mid] > target:
            #         right = mid
            #     else:
            #         left = mid
            if A[mid] >= A[left]:
                if A[mid] > target >= A[left]:
                    right = mid
                else:
                    left = mid
            else:
                if A[right] >= target > A[mid]:
                    left = mid
                else:
                    right = mid
        if target in (A[right], A[left]):
            return True
        else:
            return False
                
                