class Solution:
    # @param {int[]} A an integer array
    # @return nothing
    def sortIntegers2(self, A):
        # Write your code here

        #TLE
        # def siftdown(start, length, A):
        #     while start < length:
        #         left = 2 * start + 1
        #         right = 2 * start + 2
        #         leftVal = A[left] if left < length else float('-inf')
        #         rightVal = A[right] if right < length else float('-inf')
        #         if A[start] > max(rightVal, leftVal):
        #             return
        #         nextId = left if leftVal > rightVal else right
        #         A[start], A[nextId] = A[nextId], A[start]
        #         start = nextId
        # length = len(A)
        # for start in range(length / 2, -1, -1):
        #     siftdown(start, length, A)

        # for i in range(length - 1, 0, -1):
        #     A[i], A[0] = A[0], A[i]
        #     siftdown(0, i, A)

        ## wrong with repeated values
        # def quickSort(start, end, A):
        #     if start >= end:
        #         return
        #     mid = (start + end) / 2
        #     left, right = start, end
        #     while left <= right:
        #         while left <= right and A[left] < A[mid]:
        #             left += 1
        #         while left <= right and A[right] > A[mid]:
        #             right -= 1
        #         if left <= right:
        #             A[left], A[right] = A[right], A[left]
        #             left += 1
        #             right -= 1
        #     quickSort(start, right, A)
        #     quickSort(left, end, A)
        # length = len(A)
        # quickSort(0, length - 1, A)

        ## wrong
        def quickSort(start, end, A):
            if start >= end:
                return
            mid = (start + end) / 2
            left, right = start, end
            # while left <= right:
            #     while left <= right and A[left] < A[mid]:
            #         left += 1
            #     while left <= right and A[right] > A[mid]:
            #         right -= 1
            #     if left <= right:
            #         A[left], A[right] = A[right], A[left]
            #         left += 1
            #         right -= 1
            pre = left
            ## OMG!! DONT USE A[mid] in the while-loop.
            target = A[mid]
            while left <= right:
                if A[left] < target:
                    A[pre], A[left] = A[left], A[pre]
                    left += 1
                    pre += 1
                elif A[left] == target:
                    left += 1
                else:
                    A[left], A[right] = A[right], A[left]
                    right -= 1
            quickSort(start, pre - 1, A)
            quickSort(right + 1, end, A)
        length = len(A)
        quickSort(0, length - 1, A)

