class Solution:
    # @param S: a list of integers
    # @return: a integer
    def triangleCount(self, S):
        # write your code here
        S.sort()
        n = len(S)
        ret = 0
        for k in range(n - 1, 1, -1):
            i, j = 0, k - 1
            while i < j:
                if S[i] + S[j] > S[k]:
                    ret += j - i
                    j -= 1
                else:
                    i += 1
        return ret