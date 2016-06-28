import heapq

class Solution:
    '''
    @param {int[]} nums an integer array
    @param {int} k an integer
    @return {int[]} the top k largest numbers in array
    '''
    def topk(self, nums, k):
        # Write your code here
        nums = map(lambda x: -1 * x, nums)
        heapq.heapify(nums)
        ans = []
        while k:
            ans.append(-1 * heapq.heappop(nums))
            k -= 1
        return ans


