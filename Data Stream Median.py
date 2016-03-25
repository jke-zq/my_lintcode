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
        
        maxlen, minlen = 0, 0
        maxheap, minheap = [], []
        ans = []
        for n in nums:
            
            if not minheap or n >= minheap[0]:
                heapq.heappush(minheap, n)
                minlen += 1
            else:
                heapq.heappush(maxheap, -1 * n)
                maxlen += 1
            if minlen - maxlen > 1:
                val = heapq.heappop(minheap)
                minlen -= 1
                heapq.heappush(maxheap, -1 * val)
                maxlen += 1
            if minlen < maxlen:
                val = -1 * heapq.heappop(maxheap)
                maxlen -= 1
                heapq.heappush(minheap, val)
                minlen += 1
            
            if minlen == maxlen:
                ans.append(-1 * maxheap[0])
            else:
                ans.append(minheap[0])
        
        return ans