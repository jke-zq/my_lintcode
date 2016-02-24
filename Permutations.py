class Solution:
    """
    @param nums: A list of Integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        # write your code here
        def helper(left, visited, tmp, ret, length):
            if left == 0:
                ret.append(tmp[::])
            else:
                for i in range(0, length):
                    if not visited[i]:
                        tmp.append(nums[i])
                        visited[i] = True
                        helper(left - 1, visited, tmp, ret, length)
                        visited[i] = False
                        tmp.pop()
        ##error
        if not nums:
            return []
        nums.sort()
        length = len(nums)
        visited = [False] * length
        tmp, ret = [], []
        helper(length, visited, tmp, ret, length)
        return ret
