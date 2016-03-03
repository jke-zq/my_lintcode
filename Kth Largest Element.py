import random
class Solution:
    # @param k & A a integer and an array
    # @return ans a integer
    def kthLargestElement(self, k, A):
        
        if not A:
            return
        left, right = 0, len(A) - 1
        while left <= right:
            pivot = random.randint(left, right)
            #change pivot
            A[right], A[pivot] = A[pivot], A[right]
            newpivot = left
            for i in range(left, right):
                if A[i] > A[right]:
                    A[newpivot], A[i] = A[i], A[newpivot]
                    newpivot += 1
                    
            A[newpivot], A[right] = A[right], A[newpivot]
            
            if newpivot + 1 == k:
                return A[newpivot]
            elif newpivot + 1 > k:
                right = newpivot - 1
            else:
                left = newpivot + 1
        # return A[left]