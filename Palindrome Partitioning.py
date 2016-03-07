class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        # write your code here
        def helper(start, length, tmp, ret, s):
            if start == length:
                ret.append(tmp[:])
            else:
                for i in range(start, length):
                    if check(start, i, s):
                        tmp.append(s[start:i + 1])
                        helper(i + 1, length, tmp, ret, s)
                        tmp.pop()
        def check(start, end, s):
            while start < end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True
        
        if not s:
            return []
        length = len(s)
        ret, tmp = [], []
        helper(0, length, tmp, ret, s)
        return ret