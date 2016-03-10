class Solution:
    # @param s : A string
    # @return : An integer
    def lengthOfLongestSubstringKDistinct(self, s, k):
        # write your code here
        
        if not s or k == 0:
            return 0
        length = len(s)
        
        back = 0
        holds = collections.defaultdict(int)
        count = 0
        ans = 0
        for front in range(length):
            if s[front] in holds:
                holds[s[front]] += 1
            else:
                # if count == k:
                    # while count == k:
                while count == k:
                    holds[s[back]] -= 1
                    if holds[s[back]] == 0:
                        holds.pop(s[back])
                        count -= 1
                    back += 1
                holds[s[front]] += 1
                count += 1
            ans = max(ans, front - back + 1)
        return ans
                