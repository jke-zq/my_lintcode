class Solution:
    # @param A: Given an integer array
    # @return: void
    def heapify(self, A):
        # write your code here
        # O(nlgN)
        # def siftup(A, index):
        #     while index > 0:
        #         parent = (index - 1) / 2
        #         if A[parent] > A[index]:
        #             A[index], A[parent] = A[parent], A[index]
        #         else:
        #             break
        #         index = parent
            
        
        # for i in range(len(A)):
        #     siftup(A, i)
        f = lambda x: 2 * x + 1
        def siftdown(A, index, length):
            left = f(index)
            while left < length:
                right = left + 1
                son = right
                if right >= length or A[right] > A[left]:
                    son = left
                if A[index] > A[son]:
                    A[son], A[index] = A[index], A[son]
                    index = son
                    left = f(son)
                else:
                    break
        if not A:
            return
        length = len(A)
        for i in range(length / 2, -1, -1):
            siftdown(A, i, length)

class Solution:
    # @param A: Given an integer array
    # @return: void
    def heapify(self, A):
        # write your code here
        
        # # NlogN
        def siftup(start, A):
            # parent = (start - 1) / 2
            while start > 0:
                parent = (start - 1) / 2
                if A[parent] > A[start]:
                    A[parent], A[start] = A[start], A[parent]
                start = parent
                # parent = (start - 1) / 2
        
        if not A:
            return A
        length = len(A)
        for i in range(length):
            siftup(i, A)
        
        # N
        # def siftdown(parent, A, length):
        #     while parent < length:
        #         left = parent * 2 + 1
        #         right = parent * 2 + 2
        #         leftVal = A[left] if left < length else float('inf')
        #         rightVal = A[right] if right < length else float('inf')
        #         if A[parent] < min(leftVal, rightVal):
        #             break
        #         changeIndex = left if leftVal < rightVal else right
        #         A[parent], A[changeIndex] = A[changeIndex], A[parent]
        #         parent = changeIndex
                
        
        # if not A:
        #     return A
        # length = len(A)
        # for i in range(length / 2, -1, -1):
        #     siftdown(i, A, length)