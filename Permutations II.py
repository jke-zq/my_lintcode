class Solution:
    """
    @param nums: A list of integers.
    @return: A list of unique permutations.
    """
    def permuteUnique(self, nums):
        # write your code here
        def helper(left, visited, tmp, ret, length):
            if left == 0:
                ret.append(tmp[::])
            else:
                for i in range(length):
                    if not visited[i]:
                        if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
                            continue
                        else:
                            tmp.append(nums[i])
                            visited[i] = True
                            helper(left - 1, visited, tmp, ret, length)
                            visited[i] = False
                            tmp.pop()
        if not nums:
            return []
        nums.sort()
        length = len(nums)
        visited = [False] * length
        tmp, ret = [], []
        helper(length, visited, tmp, ret, length)
        return ret