class Solution:
    """
    @param num, a list of integer
    @return an integer
    """
    def longestConsecutive(self, num):
        # write your code here
        
        if not num:
            return 0
        
        dicts = {}
        for n in num:
            dicts[n] = 1
        
        for k in dicts.keys():
            if k not in dicts:
                continue
            nk = k + 1
            while nk in dicts:
                dicts[k] += 1
                dicts.pop(nk)
                nk += 1
            nk = k - 1
            while nk in dicts:
                dicts[k] += 1
                dicts.pop(nk)
                nk -= 1
                
            
            
        return max(dicts.values())