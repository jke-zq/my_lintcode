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


class Solution:
    """
    @param num: A list of integers
    @return: An integer
    """
    def longestConsecutive(self, num):
        # write your code here



        sets = set(num)
        length = len(sets)
        ans = 1
        for key in num:
            count = 1
            left = key - 1
            while left in sets:
                count += 1
                # TLE if not
                sets.remove(left)
                left -= 1
            right = key + 1
            while right in sets:
                count += 1
                sets.remove(right)
                right += 1
            ans = max(ans, count)
        return ans
