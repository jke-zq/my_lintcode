class Solution:
    # @param {int[]} A an integer array
    # @param {int} target an integer
    # @param {int} k a non-negative integer
    # @return {int[]} an integer array
    def kClosestNumbers(self, A, target, k):
        # Write your code here
        if not A:
            return []
            
        left, right = 0, len(A) - 1
        while left + 1 < right:
            mid = left + (right - left) / 2
            if A[mid] >= target:
                right = mid
            else:
                left = mid
            
        ret = []    
        while k and left >= 0 and right < len(A):
            if A[right] - target < target - A[left]:
                ret.append(A[right])
                right += 1
            else:
                ret.append(A[left])
                left -= 1
            k -= 1
        while k and left >= 0:
            ret.append(A[left])
            left -= 1
            k -= 1
        while k and right < len(A):
            ret.append(A[right])
            right += 1
            k -= 1
        return ret