class Solution:
    # @param {int} n a positive integer
    # @return {int[][]} n x 3 matrix
    def consistentHashing(self, n):
        # Write your code here
        def addOne(ans, count):
            maxInterVal = 0
            index = -1
            number = -1
            for i, (k, v, n) in enumerate(ans):
                if maxInterVal < v - k or (maxInterVal == v - k and number > n):
                    index = i
                    number = n
                    maxInterVal = v - k
            
            x, y, __ = ans[index]
            ans[index][1] = (x + y) / 2
            ans.insert(index + 1, [ans[index][1] + 1, y, count])
            
        ans = [[0, 359, 1]]
        count = 2
        while count <= n:
            addOne(ans, count)
            count += 1
        return ans