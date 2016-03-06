class Solution:
    """
    @param triangle: a list of lists of integers.
    @return: An integer, minimum path sum.
    """
    def minimumTotal(self, triangle):
        # write your code here
        if not triangle:
            return 0
        # ret = []
        # length = len(triangle)
        # from top to bottom
        # for i in range(length):
        #     ret.append(triangle[i][i])
        #     if i > 0:
        #         ret[-1] += ret[-2]
        #     for j in range(i - 1, 0, -1):
        #         ret[j] = min(ret[j - 1], ret[j]) + triangle[i][j]
        #     if i > 0:
        #         ret[0] += triangle[i][0]
        # return min(ret)
        
        # from bottom to top
        length = len(triangle)
        ret = [0] * length
        ret[:] = triangle[length - 1]
        for i in range(length - 2, -1, -1):
            for j in range(i + 1):
                ret[j] = min(ret[j], ret[j + 1]) + triangle[i][j]
        return ret[0]