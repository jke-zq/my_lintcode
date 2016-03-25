class Solution:
    # @param {int[][]} matrix an integer matrix
    # @return {int[][]} the coordinate of the left-up and right-down number
    def submatrixSum(self, matrix):
        # Write your code here
        def find(nums, leftR, rightR, ans):
            length = len(nums)
            presum = [0] * length
            presum[0] = nums[0]
            for i in range(1, length):
                presum[i] = presum[i - 1] + nums[i]
            
            dicts = {}
            for i in range(0, length):
                if presum[i] == 0:
                    ans.append((leftR, 0))
                    ans.append((rightR, i))
                    return True
                elif  presum[i] in dicts:
                    ans.append((leftR, dicts[presum[i]] + 1))
                    ans.append((rightR, i))
                    return True
                else:
                    dicts[presum[i]] = i
            return False
        if not matrix or not matrix[0]:
            return None
        Rows = len(matrix)
        Cols = len(matrix[0])
        ans = []
        for i in range(Rows):
            presum = [0] * Cols
            for j in range(i, Rows):
                for s in range(Cols):
                    presum[s] += matrix[j][s]
                if find(presum, i, j, ans):
                    return ans
        return None

 # [[0]]

                 # if presum[i] == 0:
                 #    ans.append((leftR, 0))
                 #    ans.append((rightR, i))
                 #    return
 #        presum = [0] * Cols
 #        ans = []
 #        for i in range(Rows - 1):
 #            presum[:] = matrix[i]
 #            for j in range(i + 1, Rows):
 #                for s in range(Cols):
 #                    presum[s] += matrix[j][s]
 #                if find(presum, i, j, ans):
 #                    return ans