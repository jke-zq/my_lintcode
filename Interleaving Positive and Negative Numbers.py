class Solution:
    """
    @param A: An integer array.
    @return nothing
    """
    def rerange(self, A):
        # write your code here
        
        if not A:
            return None
        length = len(A)
        tag = 1
        ### reduce must be init
        positive = reduce(lambda x, y: x + 1 if y > 0 else x, A, 0)
        if 2 * positive > length:
            tag = -1
        # tranf = lambda x: (1 + 2 * x) % (length | 1)
        # left, right, pivot = 0, length - 1, 0
        
        # while left <= right:
        #     leftIndex = tranf(left)
        #     # print leftIndex
        #     if tag * A[leftIndex] > 0:
        #         pivotIndex = tranf(pivot)
        #         A[pivotIndex], A[leftIndex] = A[leftIndex], A[pivotIndex]
        #         pivot += 1
        #         left += 1
        #     else:
        #         rightIndex = tranf(right)
        #         A[rightIndex], A[leftIndex] = A[leftIndex], A[rightIndex]
        #         right -= 1
        left, pivot, right = 0, 0, length - 1
        while left <= right:
            if tag * A[left] > 0:
                A[pivot], A[left] = A[left], A[pivot]
                pivot += 1
                left += 1
            else:
                A[right], A[left] = A[left], A[right]
                right -= 1
        if length % 2 == 1:
            A[0], A[pivot] = A[pivot], A[0]
            pivot = 2
            mirpivot = length - 2
        else:
            mirpivot = length - 2
            pivot = 1
        while pivot <= mirpivot:
            A[pivot], A[mirpivot] = A[mirpivot], A[pivot]
            pivot += 2
            mirpivot -= 2