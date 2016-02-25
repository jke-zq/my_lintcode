class Solution:
    # @param {int[]} A an integer array sorted in ascending order
    # @param {int} target an integer
    # @return {int} an integer
    def totalOccurrence(self, A, target):
        # Write your code here
        
        if not A:
            return 0
            
        left, right = 0, len(A)
        while left + 1 < right:
            mid = left + (right - left) / 2
            if A[mid] >= target:
                right = mid
            else:
                left = mid
        
        start = left
        if A[left] == target:
            start -= 1
        
        left, right = 0, len(A) - 1
        while left + 1 < right:
            mid = left + (right - left) / 2
            if A[mid] > target:
                right = mid
            else:
                left = mid
                
        end = right
        if A[right] == target:
            end += 1
        ##error
        #return end - start
        return end - start - 1 if end > start else 0