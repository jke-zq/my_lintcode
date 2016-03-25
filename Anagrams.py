class Solution:
    # @param strs: A list of strings
    # @return: A list of strings
    def anagrams(self, strs):
        # write your code here
        def add(hashstr, s):
            ss = list(s)
            ss.sort()
            ns = ''.join(ss)
            ns.strip()
            hashstr[ns].add(s)
            
            
        hashstr = collections.defaultdict(set)
        for s in strs:
            add(hashstr, s)
        
        ans = []
        for k, v in hashstr.items():
            if len(v) > 1:
                ans.extend(v)
        return ans
            