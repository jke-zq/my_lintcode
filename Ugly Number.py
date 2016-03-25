import heapq
class Solution:
    """
    @param k: The number k.
    @return: The kth prime number as description.
    """
    def kthPrimeNumber(self, k):
        # write your code here
        Factors = [3, 5, 7]
        heap = [1]
        sets = set()
        for __ in range(k):
            cur = heapq.heappop(heap)
            for f in Factors:
                if cur * f not in sets:
                    heapq.heappush(heap, cur * f)
                    sets.add(cur * f)
        return heapq.heappop(heap)
        
        