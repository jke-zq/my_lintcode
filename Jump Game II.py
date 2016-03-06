class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        # write your code here
        if not A:
            return 
        # step = [-1] * len(A)
        # step[0] = 0
        # for i in range(1, len(A)):
        #     ## TLE
        #     # for j in range(i - 1, -1, -1):
        #     #     if A[j] >= i - j and step[j] != float('inf'):
        #     #         step[i] = min(step[i], step[j] + 1)
        #     ## TLE too.
        #     for j in range(0, i):
        #         if A[j] >= i - j and step[j] != -1:
        #             step[i] = step[j] + 1
        #             break
        # return step[-1]
        
        ## AC
        length = len(A)
        steps = [0] * length
        steps[1] = A[0]
        if steps[1] >= length:
            return 1
        for i in range(2, length):
            for j in range(steps[i - 2], steps[i - 1] + 1):
                steps[i] = max(steps[i], j + A[j])
                if steps[i] >= length - 1:
                    return i
        # return count
            
        
        