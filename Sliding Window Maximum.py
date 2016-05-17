class Solution:
    """
    @param nums: A list of integers.
    @return: The maximum number inside the window at each moving.
    """
    def maxSlidingWindow(self, nums, k):
        # write your code here
        if not nums:
            return []
        deque = []
        # print deque
        ret = []
        for i in range(0, len(nums)):
            # while deque and deque[-1] > i - k and nums[deque[-1]] < nums[i]:
            while deque and nums[deque[-1]] < nums[i]:
                deque.pop()
            deque.append(i)
            if i >= k - 1:
                ret.append(nums[deque[0]])
                if deque[0] == i - k + 1:
                    deque.pop(0)
                
        return ret


## Solution two:
import collections
class Solution:
    """
    @param nums: A list of integers.
    @return: The maximum number inside the window at each moving.
    """
    def maxSlidingWindow(self, nums, k):
        # write your code here
        if not nums:
            return []
        deque = collections.deque()
        # print deque
        ret = []
        for i in range(len(nums)):
            # while deque and deque[-1] > i - k and nums[deque[-1]] < nums[i]:
            while deque and deque[-1] < nums[i]:
                deque.pop()
            deque.append(nums[i])
            if i >= k - 1:
                ret.append(deque[0])
                if deque[0] == nums[i - k + 1]:
                    deque.popleft()
                
        return ret