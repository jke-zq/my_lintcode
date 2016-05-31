import heapq
class Solution:
    """
    @param {int} n an integer.
    @return {int} the nth prime number as description.
    """
    def nthUglyNumber(self, n):
        # write your code here
        
        ans = [1]
        factors = [2, 3, 5]
        times = [0] * len(factors)
        values = []
        for i in range(len(factors)):
            heapq.heappush(values, (factors[i], i))
        
        while len(ans) < n:
            v, index = heapq.heappop(values)
            times[index] += 1
            if v != ans[-1]:
                ans.append(v)
            heapq.heappush(values, (factors[index] * ans[times[index]], index))
        return ans[-1]
        
        

