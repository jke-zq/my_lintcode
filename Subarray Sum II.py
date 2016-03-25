class Solution:
    # @param {int[]} A an integer array
    # @param {int} start an integer
    # @param {int} end an integer
    # @return {int} the number of possible answer
    def subarraySumII(self, A, start, end):
        # Write your code here
        def dc(presum, left, right, start, end):
            if left > right:
                return 0
            if left == right:
                return int(start <= presum[left] <= end)
            mid = left + (right - left) / 2
            leftAns = dc(presum, left, mid, start, end)
            rightAns = dc(presum, mid + 1, right, start, end)
            ## mid + 1 ~ right - left ~ mid
            ans = 0
            tmp = []
            low, j, up = mid + 1, mid + 1, mid + 1
            for i in range(left, mid + 1):
                while low <= right and presum[low] - presum[i] < start:
                    low += 1
                while up <= right and presum[up] - presum[i] <= end:
                    up += 1
                ans += up - low

                while presum[i] > presum[j]:
                    tmp.append(presum[j])
                    j += 1
                tmp.append(presum[i])
            
            presum[left:left + len(tmp)] = tmp
            return ans + leftAns + rightAns
                        
                
        if not A:
            return 0
        length = len(A)
        
        presum = [0] * length
        presum[0] = A[0]
        for i in range(1, length):
            presum[i] = presum[i - 1] + A[i]
        return dc(presum, 0, length - 1, start, end)