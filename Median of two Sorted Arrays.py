class Solution:
    """
    @param A: An integer array.
    @param B: An integer array.
    @return: a double whose format is *.5 or *.0
    """
    def findMedianSortedArrays(self, A, B):
        # write your code here
        def findKth(k, A, startA, lenA, B, startB, lenB):
            # if A is None or lenA == 0:
            #     return B[startB + k - 1]
            # if B is None or lenB == 0:
            #     return A[startA + k - 1]
            # if lenA > lenB:
            #     return findKth(k, B, startB, lenB, A, startA, lenA)
            # ## k / 2 should be positive
            # if k == 1:
            #     return min(A[startA], B[startB])
            # ## B left is more
            # if lenA < k / 2:
            #     indexA = startA + lenA - 1
            #     indexB = startB + (k - lenA) - 1
            # else:
            #     indexB = startB + (k + 1) / 2 - 1
            #     indexA = startA + k / 2 - 1
            # if B[indexB] > A[indexA]:
            #     passLen = indexA - startA + 1
            #     return findKth(k - passLen, A, indexA + 1, lenA - passLen, B, startB, lenB)
            # elif B[indexB] < A[indexA]:
            #     passLen = indexB - startB + 1
            #     return findKth(k - passLen, A, startA, lenA, B, indexB + 1, lenB - passLen)
            # else:
            #     return A[indexA]
            if startA == lenA:
                return B[startB + k - 1]
            if startB == lenB:
                return A[startA + k - 1]
            if k == 1:
                return min(A[startA], B[startB])
            valA = A[startA + k / 2 - 1] if startA + k / 2 - 1 < lenA else float('inf')
            valB = B[startB + k / 2 - 1] if startB + k / 2 - 1 < lenB else float('inf')
            if valA < valB:
                return findKth(k - k / 2, A, startA + k / 2, lenA, B, startB, lenB)
            else:
                return findKth(k - k / 2, A, startA, lenA, B, startB + k / 2, lenB)

        lenA = len(A) if A is not None else 0
        lenB = len(B) if B is not None else 0
        
        length = (lenA + lenB)
        if length % 2 == 1:
            return findKth(length / 2 + 1, A, 0, lenA, B, 0, lenB) / 1.0
        else:
            return ((findKth(length / 2, A, 0, lenA, B, 0, lenB) 
                     + 
                     findKth(length / 2 + 1, A, 0, lenA, B, 0, lenB)) / 2.0)