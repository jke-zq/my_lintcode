import heapq
class Solution:
    """
    @param nums: A list of integers.
    @return: The median of numbers
    """
    def medianII(self, nums):
        # write your code here

        if not nums:
            return []

        ans = []
        maxHeap = []
        maxLen = 0
        minHeap = []
        minLen = 0
        for n in nums:
            if not minHeap or minHeap[0] < n:
                heapq.heappush(minHeap, n)
                minLen += 1
            else:
                heapq.heappush(maxHeap, -1 * n)
                maxLen += 1
            if minLen > maxLen + 1:
                val = heapq.heappop(minHeap)
                minLen -= 1
                heapq.heappush(maxHeap, -1 * val)
                maxLen += 1
            if maxLen > minLen:
                val = heapq.heappop(maxHeap)
                maxLen -= 1
                heapq.heappush(minHeap, -1 * val)
                minLen += 1
            if minLen == maxLen:
                ans.append(maxHeap[0] * -1)
            else:
                ans.append(minHeap[0])
        return ans
