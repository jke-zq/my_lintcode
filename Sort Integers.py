class Solution:
    # @param {int[]} A an integer array
    # @return nothing
    def sortIntegers(self, A):
        # Write your code here

        def bubbleSort(A):
            length = len(A)
            for i in range(length - 1):
                for j in range(0, length - i - 1):
                    if A[j] > A[j + 1]:
                        A[j], A[j + 1] = A[j + 1], A[j]
        if not A:
            return
        bubbleSort(A)
