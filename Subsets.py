class Solution:
    """
    @param S: The set of numbers.
    @return: A list of lists. See example.
    """
    def subsets(self, S):
        # write your code here
        def helper(start, tmp, ret, length):
            ret.append(tmp[::])
            for i in range(start, length):
                tmp.append(S[i])
                helper(i + 1, tmp, ret, length)
                tmp.pop()
        
        S.sort()
        length = len(S)
        tmp, ret = [], []
        helper(0, tmp, ret, length)
        return ret