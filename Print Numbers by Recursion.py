class Solution:
    # @param n: An integer.
    # return : A list of integer storing 1 to the largest number with n digits.
    def numbersByRecursion(self, n):
        # write your code here
        def helper(depth, n, result):
            if depth == n:
                return
            
            expVal = (10 ** depth)
            length = expVal
            for mul in range(1, 10):
                for i in range(length):
                    result.append(result[i] + expVal * mul)
            helper(depth + 1, n, result)
        
        result = [0]
        helper(0, n, result)
        return result[1:]
            