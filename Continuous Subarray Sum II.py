class Solution:
    # @param {int[]} A an integer array
    # @return {int[]}  A list of integers includes the index of the 
    #                  first number and the index of the last number
    def continuousSubarraySumII(self, A):
        # Write your code here
        
        def getMax(A, length):
            ans = None
            start = -1
            gl, local = float('-inf'), float('-inf')
            for i in range(length):
                if A[i] + local < A[i]:
                    local = A[i]
                    start = i
                else:
                    local += A[i]
                if gl < local:
                    gl = local
                    ans = [start, i]
            return (gl, ans)
        def getMin(A, length):
            ans = None
            start = -1
            gl, local = float('inf'), float('inf')
            for i in range(length):
                if A[i] + local > A[i]:
                    local = A[i]
                    start = i
                else:
                    local += A[i]
                if gl > local:
                    gl = local
                    ans = [start, i]
            return (gl, ans)
        if not A:
            return None
        length = len(A)
        maxVal, maxIndex = getMax(A, length)
        total = sum(A)
        minVal, minIndex = getMin(A, length)
        # print maxVal, minVal, total
        if total == minVal or maxVal >= total - minVal:
            return maxIndex
        else:
            return [(minIndex[1] + 1) % length, (minIndex[0] - 1 + length) % length]
        