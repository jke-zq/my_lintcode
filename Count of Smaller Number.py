class Solution:
    """
    @param A: A list of integer
    @return: The number of element in the array that 
             are smaller that the given integer
    """
    def countOfSmallerNumber(self, A, queries):
        # write your code here
        
        def findFirstGreater(val, A):
            if not A:
                return 0
            left, right = 0, len(A)
            while left + 1 < right:
                mid = left + (right - left) / 2
                if A[mid] >= val:
                    right = mid
                else:
                    left = mid
            
            if A[left] >= val:
                return 0
            if A[right] < val:
                return len(A)
            return left + 1
                
        if not queries:
            return []
        ans = []
        A = sorted(A)
        for val in queries:
            ans.append(findFirstGreater(val, A))
        return ans