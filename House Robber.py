class Solution:
    # @param A: a list of non-negative integers.
    # return: an integer
    def houseRobber(self, A):
        # write your code here
        
        # f(i) = max(f(i - 1), f(i - 2) + A[i])
        # a, b = 0, 0
        # for num in A:
        #     a, b = b, max(a + num, b)
        # return b
        # array
        length = len(A)
        ret = [0] * (length + 2)
        for i in range(2, length + 2):
            ret[i] = max(ret[i - 1], ret[i - 2] + A[i - 2])
        return ret[length + 1]