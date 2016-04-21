import heapq
class Solution:
    # @param {int[]} A an integer arrays sorted in ascending order
    # @param {int[]} B an integer arrays sorted in ascending order
    # @param {int} k an integer
    # @return {int} an integer
    def kthSmallestSum(self, A, B, k):
        # Write your code here
        if not A and not B:
            return None
        lenA = len(A) if A else 0
        lenB = len(B) if B else 0
        if lenA > lenB:
            return self.kthSmallestSum(B, A, k)
        # if lenA + lenB < k:
        #     return A[-1] + B[-1]
        count = min(lenA, lenB, k)
        heap = []
        for i in range(count):
            heapq.heappush(heap, (A[i] + B[0], i, 0))
        
        while k > 1:
            __, x, y = heapq.heappop(heap)
            y += 1
            if y < lenB:
                heapq.heappush(heap, (A[x] + B[y], x, y))
            k -= 1
        
        ret, __, __ = heapq.heappop(heap)
        return ret
        
        
            
        