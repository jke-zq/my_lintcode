class Solution:
    """
    @param nums: A list of integers
    @param k: An integer denote to find k non-overlapping subarrays
    @return: An integer denote the sum of max k non-overlapping subarrays
    """
    def maxSubArray(self, nums, k):
        # write your code here
        
        ## global[i][j], to i index and j subarrays 
        ## local[i][j].
        ## global[i][j] = max(global[i - 1][j], local[i][j])
        ## local[i][j] = max(global[i - 1][j - 1] + nums[i], local[i - 1][j] + nums[i]
        
        length = len(nums)
        ## reduce the space complexity
        gl = [[float('-inf')] * (k + 1) for __ in range(2)]
        local = [[float('-inf')] * (k + 1) for __ in range(2)]
        ##gl = [float('-inf')] * (k + 1)
        ##local = [float('-inf')] * (k + 1)
        # gl = [[float('-inf')] * (k + 1) for __ in range(length)]
        # local = [[float('-inf')] * (k + 1) for __ in range(length)]
        gl[0][0] = 0
        local[0][0] = 0
        ##gl[0] = 0
        ##local[0] = 0
        # gl[0][0] = 0
        # local[0][0] = 0
        gl[0][1] = nums[0]
        local[0][1] = nums[0]
        ##gl[1] = nums[0]
        ##local[1] = nums[0]
        # for i in range(1, k + 1):
        #     if i == 1:
        #         local[0][i] = nums[0]
        #         gl[0][i] = nums[0]
        
        for i in range(1, length):
            gl[i % 2][0] = 0
            local[i % 2][0] = 0
            ##local[0] = 0
            ##gl[0] = 0
            # local[i][0] = 0
            # gl[i][0] = 0
            for j in range(1, k + 1):
                local[i % 2][j] = max(gl[(i - 1) % 2][j - 1] + nums[i], local[(i - 1) % 2][j] + nums[i])
                gl[i % 2][j] = max(gl[(i - 1) % 2][j], local[i % 2][j])
            ##for j in range(k, 0, -1):
            ##    local[j] = max(gl[j - 1] + nums[i], local[j] + nums[i])
            ##    gl[j] = max(gl[j], local[j])
            # for j in range(1, k + 1):
            #     local[i][j] = max(gl[i - 1][j - 1] + nums[i], local[i - 1][j] + nums[i])
            #     gl[i][j] = max(local[i][j], gl[i - 1][j])
        return gl[(length - 1) % 2][k]
        ##return gl[k]
        # return gl[length - 1][k]


## Solution Two
class Solution:
    """
    @param nums: A list of integers
    @param k: An integer denote to find k non-overlapping subarrays
    @return: An integer denote the sum of max k non-overlapping subarrays
    """
    def maxSubArray(self, nums, k):
        # write your code here
        
        length = len(nums)
        table = [[float('-inf')] * (k + 1) for __ in range(length + 1)]
        table[0][0] = 0
        for i in range(1, length + 1):
            table[i][0] = 0
            for j in range(1, k + 1):
                ## TLE
                local = float('-inf')
                maxs = float('-inf')
                for s in range(i - 1, -1, -1):
                    local = max(local + nums[s], nums[s])
                    maxs = max(local, maxs)
                    table[i][j] = max(table[i][j], table[s][j - 1] + maxs)
                ## TLE    
                # local = float('-inf')
                # maxVal = float('-inf')
                # for s in range(0, i):
                #     local = float('-inf')
                #     maxVal = float('-inf')
                #     for x in range(s + 1, i + 1):
                #         local = max(local + nums[x - 1], nums[x - 1])
                #         maxVal = max(maxVal, local)
                # table[i][j] = max(table[i][j], table[s][j - 1] + maxVal)
        # length = len(nums)
        # table = [[float('-inf')] * (length + 1) for __ in range(length + 1)]
        # table[0][0] = 0
        # for i in range(1, length + 1):
        #     table[i][0] = 0
        #     for j in range(1, min(i, k) + 1):
        #         table[i][j] = table[i - 1][j]
        #         maxp = 0
        #         for p in range(i, j - 1, -1):
        #             maxp = max(0, maxp) + nums[p - 1]
        #             table[i][j] = max(table[i][j], table[p - 1][j - 1] + maxp)
                    
        return table[length][k]


## Solution:
class Solution:
    """
    @param nums: A list of integers
    @param k: An integer denote to find k non-overlapping subarrays
    @return: An integer denote the sum of max k non-overlapping subarrays
    """
    def maxSubArray(self, nums, k):
        # write your code here
        
        if not nums:
            return 0
        length = len(nums)
        local = [[float('-inf')] * (k + 1) for __ in range(1 + length)]
        gl = [[float('-inf')] * (k + 1) for __ in range(1 + length)]
        local[0][0] = 0
        gl[0][0] = 0
        for i in range(1, length + 1):
            # diff = nums[i] - nums[i - 1]
            local[i][0] = 0
            gl[i][0] = 0
            diff = nums[i - 1]
            for j in range(1, k + 1):
                local[i][j] = max(gl[i - 1][j - 1] + diff, local[i - 1][j] + diff)
                gl[i][j] = max(gl[i - 1][j], local[i][j])
        # print local
        # print gl
        return gl[length][k]