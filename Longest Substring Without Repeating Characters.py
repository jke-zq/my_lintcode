class Solution:
    # @param s: a string
    # @return: an integer
    def lengthOfLongestSubstring(self, s):
        # write your code here
        
        # length = len(s)
        # sets = set()
        # pre, post = 0, 0
        # ans = 0
        # # while pre < length:
        # for pre in range(length):
        #     if s[pre] not in sets:
        #         sets.add(s[pre])
        #         # pre += 1
        #         ans = max(ans, pre - post + 1)
        #     else:
        #         # ans = max(ans, len(sets))
        #         while s[post] != s[pre]:
        #             sets.remove(s[post])
        #             post += 1
        #         # sets.remove(s[post])
        #         post += 1
        #         # pre += 1
                
            
        # # ans = max(ans, len(sets))
            
        # return ans
        length = len(s)
        sets = set()
        j = 0
        ans = 0
        for i in range(length):
            while j < length and s[j] not in sets:
                sets.add(s[j])
                ans = max(ans, j - i + 1)
                j += 1
            if s[i] in sets:
                sets.remove(s[i])
        return ans
                