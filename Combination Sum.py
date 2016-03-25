class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        # write your code here
        def helper(start, left, tmp, ret, candidates, length):
            if left == 0:
                ret.append(tmp[:])
                return
            else:
                for i in range(start, length):
                    if candidates[i] > left:
                        break
                    else:
                        tmp.append(candidates[i])
                        helper(i, left - candidates[i], tmp, ret, candidates, length)
                        tmp.pop()
        if not candidates:
            return []
        candidates.sort()
        tmp, ret = [], []
        helper(0, target, tmp, ret, candidates, len(candidates))
        
        return ret