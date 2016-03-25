class Solution:
    # @param {int[]} A an integer array
    # @return {int[]}  A list of integers includes the index of the 
    #                  first number and the index of the last number
    def continuousSubarraySum(self, A):
        # Write your code here
        if not A:
            return []
        length = len(A)
        ans = [-1, -1]
        pre = -1
        local, gl = float('-inf'), float('-inf')
        for i in range(length):
            if local + A[i] < A[i]:
                local = A[i]
                pre = i
            else:
                local += A[i]
            if gl < local:
                gl = local
                ans[0] = pre
                ans[1] = i
        return ans
        