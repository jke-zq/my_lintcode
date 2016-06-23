import heapq
class Solution:
    # @param {int[][]} arrays a list of array
    # @param {int} k an integer
    # @return {int} an integer, K-th largest element in N arrays
    def KthInArrays(self, arrays, k):
        # Write your code here
        
        minHeap = []
        for array in arrays:
            minHeap.extend(map(lambda x: -1 * x, array))
        heapq.heapify(minHeap)
        while k > 1:
            heapq.heappop(minHeap)
            k -= 1
        
        return -1 * heapq.heappop(minHeap)