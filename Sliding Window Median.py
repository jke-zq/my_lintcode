import heapq
class Solution:
    """
    @param nums: A list of integers.
    @return: The maximum number inside the window at each moving.
    """
    def medianSlidingWindow(self, nums, k):
        # write your code here
        minLen, minheap = 0, []
        maxLen, maxheap = 0, []
        mid = 0
        ret = []
        for i in range(len(nums)):

            if not minheap or nums[i] >= minheap[0]:
                heapq.heappush(minheap, nums[i])
                minLen += 1
            else:
                heapq.heappush(maxheap, -1 * nums[i])
                maxLen += 1
            while minLen > maxLen + 1:
                mid = heapq.heappop(minheap)
                minLen -= 1
                heapq.heappush(maxheap, -1 * mid)
                maxLen += 1
            while minLen < maxLen:
                mid = -1 * heapq.heappop(maxheap)
                maxLen -= 1
                heapq.heappush(minheap, mid)
                minLen += 1
            if i >= k - 1:
                if maxLen == minLen:
                    ret.append(-1 * maxheap[0])
                else:
                    ret.append(minheap[0])
            
                if -1 * nums[i - k + 1] in maxheap:
                    maxheap.remove(-1 * nums[i - k + 1])
                    heapq.heapify(maxheap)
                    maxLen -= 1
                elif nums[i - k + 1] in minheap:
                    minheap.remove(nums[i - k + 1])
                    heapq.heapify(minheap)
                    minLen -= 1
        return ret
#note
#without heapq.remove
#not hash to find the index