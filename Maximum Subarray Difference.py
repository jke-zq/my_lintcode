class Solution:
    """
    @param nums: A list of integers
    @return: An integer indicate the value of maximum difference between two
             Subarrays
    """
    def maxDiffSubArrays(self, nums):
        # write your code here
        if not nums:
            return 0
        length = len(nums)
        leftMins = [0] * length
        leftMaxs = [0] * length
        globalMin, localMin = float('inf'), float('inf')
        globalMax, localMax = float('-inf'), float('-inf')
        for i in range(length):
            ## leftMin
            localMin = min(localMin + nums[i], nums[i])
            globalMin = min(globalMin, localMin)
            leftMins[i] = globalMin
            ## leftMax
            localMax = max(localMax + nums[i], nums[i])
            globalMax = max(localMax, globalMax)
            leftMaxs[i] = globalMax
        
        rightMins = [0] * length
        rightMaxs = [0] * length
        globalMin, localMin = float('inf'), float('inf')
        globalMax, localMax = float('-inf'), float('-inf')   
        for i in range(length - 1, -1, -1):
            ## rightMins
            localMin = min(localMin + nums[i], nums[i])
            globalMin = min(globalMin, localMin)
            rightMins[i] = globalMin
            ## rightaxs
            localMax = max(localMax + nums[i], nums[i])
            globalMax = max(localMax, globalMax)
            rightMaxs[i] = globalMax 
        ans = float('-inf')
        for i in range(length - 1):
            ans = max(ans, abs(leftMins[i] - rightMaxs[i + 1]), abs(leftMaxs[i] - rightMins[i + 1]))
        return ans
