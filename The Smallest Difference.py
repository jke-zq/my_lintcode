class Solution:
    # @param A, B: Two lists of integer
    # @return: An integer
    def smallestDifference(self, A, B):
        # write your code here
        
        A.sort()
        B.sort()
        one, two = 0, 0
        
        lenA, lenB = len(A), len(B)
        ans = float('inf')
        while one < lenA and two < lenB:
            ans = min(ans, abs(A[one] - B[two]))
            if A[one] > B[two]:
                two += 1
            else:
                one += 1
        return ans