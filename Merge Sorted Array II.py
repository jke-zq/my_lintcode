class Solution:
    #@param A and B: sorted integer array A and B.
    #@return: A new sorted integer array
    def mergeSortedArray(self, A, B):
        # write your code here
        if not A:
            return B
        if not B:
            return A
            
        ans = []
        lenA, lenB = len(A), len(B)
        i, j = 0, 0
        while i < lenA and j < lenB:
            if A[i] < B[j]:
                ans.append(A[i])
                i += 1
            else:
                ans.append(B[j])
                j += 1
        if j < lenB:
            ans.extend(B[j:])
        if i < lenA:
            ans.extend(A[i:])
        return ans
        
        