class Solution:    
    """
    @param candidates: Given the candidate numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
    """
    def combinationSum2(self, candidates, target): 
        # write your code here
        def helper(start, left, tmp, ret, candidates, length):
            if left == 0:
                ret.append(tmp[:])
                return
            else:
                for i in range(start, length):
                    if i > start and candidates[i] == candidates[i - 1]:
                        continue
                    else:
                        if candidates[i] > left:
                            continue
                        else:
                            tmp.append(candidates[i])
                            helper(i + 1, left - candidates[i], tmp, ret, candidates, length)
                            tmp.pop()
        
        
        if not candidates:
            return []
        candidates.sort()
        length = len(candidates)
        ret, tmp = [], []
        helper(0, target, tmp, ret, candidates, length)
        return ret