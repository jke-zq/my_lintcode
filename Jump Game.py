class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        # write your code here
        
        if not A:
            return
        length = len(A)
        ret = [0] * length
        ret[0] = A[0]
        for i in range(1, length):
            if ret[i - 1] < i:
                return False
            ret[i] = max(ret[i - 1], i + A[i])
        return True