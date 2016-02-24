class Solution:
    """
    @param S: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, S):
        # write your code here
        def helper(start, tmp, ret):
            ret.append(tmp[::])
            for i in range(start, len(S)):
                if i > start and S[i] == S[i - 1]:
                    continue
                else:
                    tmp.append(S[i])
                    helper(i + 1, tmp, ret)
                    tmp.pop()
       
        S.sort()
        tmp, ret = [], []
        helper(0, tmp, ret)
        return ret