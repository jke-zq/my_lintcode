import operator
class Solution:
    # @param {int[]} A an array of Integer
    # @return {int}  an integer
    def longestIncreasingContinuousSubsequence(self, A):
        # Write your code here
        # ans = 1
        # if not A:
        #     return 0
        # ans1 = 1
        # for i in range(1, len(A)):
        #     if A[i] >= A[i - 1]:
        #         ans1 += 1
        #     else:
        #         ans1 = 1
        #     ans = max(ans1, ans)
        # ans2 = 1
        # for i in range(1, len(A)):
        #     if A[i] < A[i - 1]:
        #         ans2 += 1
        #     else:
        #         ans2 = 1
        #     ans = max(ans, ans2)
        # return ans
        
        # def searchInc(start, inc, A, length, op):
        #     if start < 0:
        #         return 0
            
        #     if inc[start] != -1:
        #         return inc[start]
                
        #     if start == 0:
        #         inc[start] = 1
        #     elif op(A[start], A[start - 1]):
        #         inc[start] = 1 + searchInc(start - 1, inc, A, length, op)
        #     else:
        #         inc[start] = 1
        #         searchInc(start - 1, inc, A, length, op)
        #     return inc[start]
            
        # if not A:
        #     return 0
        # length = len(A)
        # inc = [-1] * length
        # dec = [-1] * length
        # searchInc(length - 1, inc, A, length, operator.gt)
        # searchInc(length - 1, dec, A, length, operator.lt)
        # return max(max(inc), max(dec))
        def search(i, dp, A, length):
            if dp[i] != 0:
                return dp[i]
            ans = 1
            if i > 0 and A[i] > A[i - 1]:
                ans = max(ans, 1 + search(i - 1, dp, A, length))
            if i + 1 < length and A[i] > A[i + 1]:
                ans = max(ans, 1 + search(i + 1, dp, A, length))
            dp[i] = ans
            return ans
        if not A:
            return 0
        length = len(A)
        dp = [0] * length
        for i in range(length):
            search(i, dp, A, length)
        return max(dp)

## solution two
        def incresing(A):
            ans = 1
            count = 1
            for index in range(1, len(A)):
                if A[index] > A[index - 1]:
                    count += 1
                else:
                    count = 1
                ans = max(ans, count)
            return ans
        def decresing(A):
            ans = 1
            count = 1
            for index in range(1, len(A)):
                if A[index] < A[index - 1]:
                    count += 1
                else:
                    count = 1
                ans = max(ans, count)
            return ans
        
        if not A:
            return 0
        return max(incresing(A), decresing(A))